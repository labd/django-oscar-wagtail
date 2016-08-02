from django.contrib.contenttypes.models import ContentType
from django.db import models
from django.utils.translation import ugettext_lazy as _
from oscar.core.loading import get_class
from wagtail.wagtailadmin.edit_handlers import (
    FieldPanel, PublishingPanel, RichTextFieldPanel)
from wagtail.wagtailcore.fields import RichTextField
from wagtail.wagtailcore.models import Page


class AbstractCategory(Page):
    is_creatable = False

    description = RichTextField(_('Description'), blank=True)
    name = models.CharField(_('Name'), max_length=255, db_index=True)
    image = models.ImageField(_('Image'), upload_to='categories', blank=True,
                              null=True, max_length=255)

    content_panels = [
        FieldPanel('title'),
        FieldPanel('name'),
        RichTextFieldPanel('description'),
    ]

    settings_panels = [
        PublishingPanel(),
    ]

    class Meta:
        abstract = True

    def save(self, *args, **kwargs):
        if not self.name:
            self.name = self.title
        return super(AbstractCategory, self).save(*args, **kwargs)

    def serve(self, request, *args, **kwargs):
        cls = get_class('catalogue.views', 'CatalogueView')
        response = cls.as_view()(request, category=self, **kwargs)
        return response

    def get_ancestors_and_self(self):
        """
        Gets ancestors and includes itself. Use treebeard's get_ancestors
        if you don't want to include the category itself. It's a separate
        function as it's commonly used in templates.
        """
        return list(self.get_ancestors()) + [self]

    def get_category_ancestors(self):
        return (
            list(
                self.get_ancestors()
                .filter(content_type=self.content_type)
                .specific()
                .order_by('depth')
            ) + [self])

    def get_descendants_and_self(self):
        """
        Gets descendants and includes itself. Use treebeard's get_descendants
        if you don't want to include the category itself. It's a separate
        function as it's commonly used in templates.
        """
        return list(self.get_descendants()) + [self]

    def has_children(self):
        return self.get_num_children() > 0

    def get_num_children(self):
        return self.get_children().count()

    def category_ancestors(self):
        content_type = ContentType.objects.get_for_model(self)
        return self.get_ancestors().filter(content_type=content_type)

    @classmethod
    def get_root_nodes(cls):
        content_type = ContentType.objects.get_for_model(cls)
        depth = (
            cls.objects
            .filter(content_type=content_type)
            .aggregate(depth=models.Min('depth')))['depth']

        if depth is not None:
            return cls.objects.filter(content_type=content_type, depth=depth)
        return cls.objects.filter(content_type=content_type)

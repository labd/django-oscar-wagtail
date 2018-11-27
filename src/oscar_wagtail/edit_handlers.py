from django.utils.html import escape
from wagtail.admin.edit_handlers import BaseChooserPanel
from wagtail.core.models import Page
from wagtail.core.rich_text.pages import PageLinkHandler as _PageLinkHandler

from oscar_wagtail import widgets


class ProductChooserPanel(BaseChooserPanel):
    object_type_name = "product"

    _target_content_type = None

    def __init__(self, field_name, product_type=None):
        super().__init__(field_name)
        self.product_type = product_type

    def clone(self):
        return self.__class__(
            field_name=self.field_name,
            product_type=self.product_type,
        )

    def widget_overrides(self):
        return {
            self.field_name: widgets.AdminProductChooser()
        }


class PageLinkHandler(_PageLinkHandler):
    """Override the default PageLinkHandler to make sure we use the url
    property of the `Category` classes.

    """

    @staticmethod
    def expand_db_attributes(attrs, for_editor):
        try:
            page = Page.objects.get(id=attrs['id']).specific
            if for_editor:
                editor_attrs = 'data-linktype="page" data-id="%d" ' % page.id
            else:
                editor_attrs = ''

            return '<a %shref="%s">' % (editor_attrs, escape(page.url))
        except Page.DoesNotExist:
            return "<a>"

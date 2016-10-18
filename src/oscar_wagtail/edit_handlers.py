from django.utils.html import escape
from wagtail.wagtailadmin.edit_handlers import BaseChooserPanel
from wagtail.wagtailcore.models import Page
from wagtail.wagtailcore.rich_text import PageLinkHandler as _PageLinkHandler

from oscar_wagtail import widgets


class BaseProductChooserPanel(BaseChooserPanel):
    object_type_name = "product"

    _target_content_type = None

    @classmethod
    def widget_overrides(cls):
        return {
            cls.field_name: widgets.AdminProductChooser()
        }


class ProductChooserPanel(object):
    def __init__(self, field_name, product_type=None):
        self.field_name = field_name
        self.product_type = product_type

    def bind_to_model(self, model):
        return type(str('_ProductChooserPanel'), (BaseProductChooserPanel,), {
            'model': model,
            'field_name': self.field_name,
            'product_type': self.product_type,
        })


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

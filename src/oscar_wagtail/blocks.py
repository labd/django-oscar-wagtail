from django.utils.functional import cached_property
from oscar.core.loading import get_model
from wagtail.wagtailcore import blocks


class ProductChooserBlock(blocks.ChooserBlock):

    @cached_property
    def target_model(self):
        return get_model('catalogue', 'Product')

    @cached_property
    def widget(self):
        from oscar_wagtail.widgets import AdminProductChooser  # cyclic import
        return AdminProductChooser

    def get_prep_value(self, value):
        if isinstance(value, int):
            return value
        return super(ProductChooserBlock, self).get_prep_value(value)

    def to_python(self, value):
        if value is None or isinstance(value, self.target_model):
            return value
        else:
            try:
                return self.target_model.objects.get(pk=value)
            except self.target_model.DoesNotExist:
                return None


class ProductListBlock(blocks.ListBlock):
    def __init__(self, *args, **kwargs):
        kwargs['child_block'] = ProductChooserBlock()
        super(ProductListBlock, self).__init__(*args, **kwargs)

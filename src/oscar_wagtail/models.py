from django.db import models
from django.utils.translation import ugettext_lazy as _
from modelcluster.fields import ParentalKey
from modelcluster.models import ClusterableModel
from wagtail.wagtailadmin.edit_handlers import (FieldPanel, InlinePanel,)
from wagtail.wagtailcore.models import Orderable
from wagtail.wagtailsnippets.models import register_snippet

from oscar_wagtail.edit_handlers import ProductChooserPanel


class ProductListSnippet(ClusterableModel):
    title = models.CharField(max_length=255)
    code = models.CharField(max_length=100, unique=True)

    panels = [
        FieldPanel('title'),
        FieldPanel('code'),
    ]

    def __unicode__(self):
        return self.title


class ProductListItem(Orderable):
    parent = ParentalKey(to=ProductListSnippet, related_name='items')
    product = models.ForeignKey('catalogue.Product', related_name='+')

    panels = [
        ProductChooserPanel('product'),
    ]


ProductListSnippet.panels += [
    InlinePanel('items', label=_("Products"))
]


register_snippet(ProductListSnippet)

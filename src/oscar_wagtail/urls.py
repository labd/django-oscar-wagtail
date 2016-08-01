from django.conf.urls import url

from oscar_wagtail import views

urlpatterns = [
    url(r'^product-choose/$',
        views.product_choose, name='product_choose'),

    url(r'^product-choose/(\d+)/$',
        views.product_chosen, name='product_chosen'),
]

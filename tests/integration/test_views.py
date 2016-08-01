import pytest

from oscar_wagtail import views


@pytest.mark.django_db
def test_product_choose(rf):
    request = rf.get('/')
    views.product_choose(request)

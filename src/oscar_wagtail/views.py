import json

from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.core.urlresolvers import reverse
from django.db.models import Q
from django.shortcuts import get_object_or_404
from django.utils.six import text_type
from oscar.core.loading import get_model
from wagtail.wagtailadmin.forms import SearchForm
from wagtail.wagtailadmin.modal_workflow import render_modal_workflow

Product = get_model('catalogue', 'Product')


def product_choose(request):

    queryset = (
        Product.objects.get_queryset()
        .browsable()
        .order_by('title')
    )

    p = request.GET.get('p', 1)

    if request.GET.get('q'):
        searchform = SearchForm(request.GET)
        if searchform.is_valid():
            cleaned_data = searchform.cleaned_data

            if hasattr(queryset, 'search'):
                queryset = queryset.search(cleaned_data['q'])
            else:
                queryset = queryset.filter(
                    Q(title__icontains=cleaned_data['q']) |
                    Q(upc__icontains=cleaned_data['q']))

    else:
        searchform = SearchForm()

    paginator = Paginator(queryset, 10)

    try:
        paginated_items = paginator.page(p)
    except PageNotAnInteger:
        paginated_items = paginator.page(1)
    except EmptyPage:
        paginated_items = paginator.page(paginator.num_pages)

    return render_modal_workflow(
        request,
        'oscar_wagtail/chooser/product_choose.html',
        'oscar_wagtail/chooser/product_choose.js',
        {
            'items': paginated_items,
            'searchform': searchform,
        }
    )


def product_chosen(request, pk):
    product = get_object_or_404(Product, pk=pk)

    product_json = json.dumps({
        'id': product.pk,
        'string': text_type(product),
        'edit_link': reverse(
            'dashboard:catalogue-product', kwargs={'pk': product.pk})
    })

    return render_modal_workflow(
        request,
        None, 'oscar_wagtail/chooser/product_chosen.js',
        {
            'product_json': product_json,
        }
    )

from django.conf import settings
from django.urls import reverse
from django.utils.html import format_html
from wagtail.admin.menu import MenuItem
from wagtail.core import hooks

from oscar_wagtail.edit_handlers import PageLinkHandler


@hooks.register('insert_editor_js')
def editor_js():
    return format_html(
        """
        <script src="{0}{1}"></script>
        <script>window.chooserUrls.productChooser = '{2}';</script>
        """,
        settings.STATIC_URL,
        'oscar_wagtail/js/product-chooser.js',
        reverse('oscar_wagtail:product_choose')
    )


@hooks.register('register_admin_menu_item')
def register_frank_menu_item():
    return MenuItem(
        'Oscar', reverse('dashboard:index'),
        classnames='icon icon-cogs', order=10000)


@hooks.register('register_rich_text_link_handler')
def override_page_link_handler():
    return 'page', PageLinkHandler

from django.conf.urls import include, url
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from wagtail.admin import urls as wagtailadmin_urls
from oscar.app import application

from oscar_wagtail import urls as oscar_wagtail_urls

admin.autodiscover()

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'', application.urls),
    url(r'^i18n/', include('django.conf.urls.i18n')),

    url(r'^dashboard/cms/', include(wagtailadmin_urls.urlpatterns)),
    url(r'^dashboard/cms/', include(oscar_wagtail_urls)),
]
urlpatterns += staticfiles_urlpatterns()

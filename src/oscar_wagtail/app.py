from django.conf.urls import include, url
from oscar.core.application import Application
from wagtail.wagtailcore import urls as wagtail_urls


class WagtailApplication(Application):

    def get_urls(self):
        urlpatterns = [
            url(r'', include(wagtail_urls)),
        ]

        return self.post_process_urls(urlpatterns)


application = WagtailApplication()

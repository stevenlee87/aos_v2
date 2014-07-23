from django.conf.urls import patterns, include, url

import xadmin
xadmin.autodiscover()

urlpatterns = patterns(
    '',
    url(r'^xadmin/', include(xadmin.site.urls)),
)

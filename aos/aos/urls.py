from django.conf.urls import patterns, include, url

import xadmin
xadmin.autodiscover()

from xadmin.plugins import xversion
xversion.register_models()

urlpatterns = patterns(
    '',
    url(r'^xadmin/', include(xadmin.site.urls)),
)

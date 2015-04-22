from django.conf.urls import patterns, include, url

import xadmin
from servicespecific import views_xmlget

xadmin.autodiscover()

from xadmin.plugins import xversion
xversion.register_models()

urlpatterns = patterns(
    '',
    url(r'^xadmin/', include(xadmin.site.urls)),
    url(r'^servicespecific/xmlget/$', views_xmlget.getAll),
)

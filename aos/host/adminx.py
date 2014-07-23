#coding:utf-8
from __future__ import unicode_literals

import xadmin

from .models import (
    Host, Service
)


class HostAdmin(object):
    reversion_enable = True

    list_display = ('id', 'name', 'ip_in', 'ip_out', 'service', 'status', 'comment','update_time')

    list_display_links = ('id', 'name')
    list_editable = ('published', 'available')

    search_fields = ('id', 'name', 'ip_in', 'ip_out')
    list_filter = ['service']


xadmin.site.register(Host, HostAdmin)
#xadmin.site.register(Host, )


class ServiceAdmin(object):
    list_display = ('id', 'name', 'host_count', 'update_time')
    list_display_links = ('id', 'name')
    def host_count(self, obj):
        return '%s台' % obj.host_set.count()
    
    host_count.short_description = '主机数量'	

xadmin.site.register(Service, ServiceAdmin)

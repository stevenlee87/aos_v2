#coding:utf-8
#from __future__ import unicode_literals
from __future__ import absolute_import, division, with_statement, unicode_literals
import xadmin

from .models import (
    Host, Service, InternetDataCenter
)

class HostInline(object):
    model = Host
    extra = 0
    style = 'accordion'
    readonly_fields = ('id', )
    can_delete = False

class HostAdmin(object):
    reversion_enable = True

    list_display = ('id', 'name', 'ip_in', 'ip_out', 'internetdatacenter', 'service', 'type', 'status', 'comment','update_time')

    list_display_links = ('id', 'name')
    list_editable = ('published', 'available')

    search_fields = ('id', 'name', 'ip_in', 'ip_out')
    list_filter = ['service']

xadmin.site.register(Host, HostAdmin)

class ServiceAdmin(object):
    inlines = [HostInline]
    reversion_enable = True
    list_display = ('id', 'name', 'host_count', 'update_time')
    list_display_links = ('id', 'name')
    def host_count(self, obj):
        return '%s台' % obj.host_set.count()
    
    host_count.short_description = '主机数量'	

xadmin.site.register(Service, ServiceAdmin)

class InternetDataCenterAdmin(object):
    inlines = [HostInline]
    reversion_enable = True
    list_display = ('id', 'name', 'idc_contact','host_count', 'comment', 'update_time')
    list_display_links = ('id', 'name')
    def host_count(self, obj):
        return '%s台' % obj.host_set.count()

    host_count.short_description = '主机数量'

xadmin.site.register(InternetDataCenter, InternetDataCenterAdmin)


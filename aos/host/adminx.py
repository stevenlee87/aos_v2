#coding:utf-8
#from __future__ import unicode_literals
from __future__ import absolute_import, division, with_statement, unicode_literals
import xadmin

from .models import (
    Host, Service, InternetDataCenter, HostComment
)

class HostInline(object):
    model = Host
    extra = 0
    style = 'accordion'
    readonly_fields = ('id', )
    can_delete = False

class HostCommentInline(object):
    model = HostComment
    extra = 0
    style = 'accordion'
    readonly_fields = ('id', )
    can_delete = True

class HostAdmin(object):
    inlines = [HostCommentInline]
    reversion_enable = True

    #list_display = ('id', 'name', 'ip_in', 'ip_out', 'internetdatacenter', 'service', 'type', 'status', 'comment','update_time')
    list_display = ('id', 'name', 'ip_in', 'ip_out', 'internetdatacenter', 'service', 'type', 'status', 'hostcomment_display', 'update_time')

    list_display_links = ('id', 'name')
    list_editable = ('published', 'available')

    search_fields = ('id', 'name', 'ip_in', 'ip_out')
    list_filter = ['service']

    def hostcomment_display(self, obj):
        item_add = ''
        i = 1
        
        for hostcomment_item in obj.hostcomment_set.all():
            content = hostcomment_item.comment

            column_number = 32
            while True:
                if len(content) > column_number:
                    content = content[0:column_number] + '<br>' + content[column_number:(column_number*2)]
                    if len(content[(column_number*2):]) > column_number:
                        #content = content[0:column_number*2] + '<br>' + content[(column_number*2):(column_number*3)] + '<br>' + content[(column_number*3):]
                        content = content[0:column_number*2] + '<br>' + content[(column_number*2):]
                        break
                    else:
                        break
                else:
                    break

            item_add += ('%s' + '.' + content + '<br>') % i
            i += 1
        return item_add

    hostcomment_display.short_description = '备注'
    hostcomment_display.allow_tags = True

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


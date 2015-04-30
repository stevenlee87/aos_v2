#coding:utf-8
#from __future__ import unicode_literals
from __future__ import absolute_import, division, with_statement, unicode_literals
import xadmin

from host.models import Host, Service
from .models import (
    #Host, Service, CloudAndService, HostComment
    #ServerList, Project
    ServerList
)

#class HostCommentInline(object):
#    model = HostComment
#    extra = 0
#    style = 'accordion'
#    readonly_fields = ('id', )
#    can_delete = True

class ServerListInline(object):
    model = ServerList
    extra = 0
    style = 'accordion'
    readonly_fields = ('id', )
#    can_delete = False
    can_delete = True

class ServerListAdmin(object):
    #inlines = [HostCommentInline]
    reversion_enable = True

    list_display = ('custom_id', 'created_time', 'service', 'game_district', 'server_group_nickname', 'host', 'aid', 'zone', 'group_name', 'unique', 'pay')

    list_display_links = ('custom_id', 'service')
    list_editable = ('published', 'available')

    #search_fields = ('custom_id', 'created_time', 'service', 'game_district', 'server_group_nickname', 'host', 'aid', 'zone', 'group_name')
    search_fields = ('custom_id', 'game_district', 'server_group_nickname', 'host', 'aid', 'zone', 'group_name', 'unique', 'pay')
    #list_filter = ['service']
    list_filter = ['custom_id', 'game_district', 'server_group_nickname', 'host', 'aid', 'zone', 'group_name', 'unique', 'pay']

xadmin.site.register(ServerList, ServerListAdmin)
#xadmin.site.register(Host, )


#class ProjectAdmin(object):
#    inlines = [ServerListInline]
#    reversion_enable = True
#    list_display = ('id', 'name')
#    list_display_links = ('id', 'name')
#
#xadmin.site.register(Project, ProjectAdmin)

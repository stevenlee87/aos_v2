#coding:utf-8
from __future__ import unicode_literals

import xadmin

from .models import (
    Host, Group
)


class HostAdmin(object):
    reversion_enable = True

    list_display = ('id', 'name', 'ip', 'group', 'update_time')

    list_display_links = ('id', 'name')
    list_editable = ('published', 'available')

    search_fields = ('id', 'name', 'ip')
    list_filter = ['group']


xadmin.site.register(Host, HostAdmin)


class GroupAdmin(object):
    list_display = ('id', 'name', 'update_time')
    list_display_links = ('id', 'name')

xadmin.site.register(Group, GroupAdmin)

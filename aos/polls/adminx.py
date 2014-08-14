#coding:utf-8
#from __future__ import unicode_literals
from __future__ import absolute_import, division, with_statement, unicode_literals

import xadmin
from xadmin import views
from xadmin.plugins.actions import ActionPlugin
from xadmin.plugins.relate import RelateMenuPlugin

from .models import (
    Choice, Poll 
)

class PollAdmin(object):
    #版本管理
    reversion_enable = True

    list_display = ('id', 'question', 'pub_date')

    list_display_links = ('id', 'question')
    list_editable = ('published', 'available')

    search_fields = ('id', 'question')
    list_filter = ['question']


xadmin.site.register(Poll, PollAdmin)
#xadmin.site.register(Host, )


class ChoiceAdmin(object):
    reversion_enable = True
    list_display = ('id', 'choice_text', 'votes', 'poll')
    list_display_links = ('id', 'choice_text')

xadmin.site.register(Choice, ChoiceAdmin)


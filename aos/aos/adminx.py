#coding:utf-8
#from __future__ import unicode_literals
from __future__ import absolute_import, division, with_statement, unicode_literals
from collections import namedtuple

import xadmin
from xadmin import views
from xadmin.plugins.actions import ActionPlugin
from xadmin.plugins.relate import RelateMenuPlugin

#from cas_auth.views import CasLoginView

ActionPlugin.global_actions = []
RelateMenuPlugin.use_related_menu = False
#xadmin.site.set_loginview(CasLoginView)

class BaseSetting(object):
    enable_themes = False
    use_bootswatch = True
xadmin.site.register(views.BaseAdminView, BaseSetting)


class GlobeSetting(object):
    site_title = '乐道互动'
xadmin.site.register(views.CommAdminView, GlobeSetting)

class NavMenuPlugin(views.BaseAdminPlugin):
    MenuBlock = namedtuple('MenuBlock', 'title items')
    MenuItem = namedtuple('MenuItem', 'title icon url')
    MenuItemReplace = namedtuple('MenuItem', 'perm title')
    target_menu = [
        MenuBlock('Host', [
            MenuItemReplace('host.view_host', '主机管理', ),
            MenuItemReplace('host.view_service', '业务框架管理', ),
            MenuItemReplace('host.view_cloudandservice', '云与服务管理', ),
        ]),
        MenuBlock('业务具体管理', [
            MenuItemReplace('servicespecific.view_serverlist', '服务器组列表', ),
            MenuItemReplace('servicespecific.view_project', '项目管理', ),
        ]),
        MenuBlock('其他', [
            MenuItemReplace('auth.view_group', '组', ),
            MenuItemReplace('auth.view_user', '用户', ),
            MenuItemReplace('auth.view_permission', '权限', ),
        ]),
    ]

    def get_nav_menu(self, navi_menu):
        menu_map = {}
        for block in navi_menu:
            for menu in block['menus']:
                menu_map[menu['perm']] = menu
    
        result_menu = []
        for block in self.target_menu:
            block_menu = {
                'title': block.title,
                'first_url': '',
                'menus': []
            }
        
            for item in block.items:
                if isinstance(item, self.MenuItem):
                    item_menu = {
                    'perm': item.title + 'perm',
                    'title': item.title,
                    'url': item.url,
                    'icon': item.icon,
                    }
                elif isinstance(item, self.MenuItemReplace):
                    item_menu = menu_map[item.perm]
                    item_menu['title'] = item.title
                else:
                    item_menu = menu_map[item]
                
                block_menu['menus'].append(item_menu)
            result_menu.append(block_menu)
        return result_menu
xadmin.site.register_plugin(NavMenuPlugin, views.CommAdminView)

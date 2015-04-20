# coding:utf-8
from __future__ import unicode_literals

from django.db import models

class Project(models.Model):
    """ 项目管理"""
    name = models.CharField(max_length=200, verbose_name="项目名称")

    update_time = models.DateTimeField(auto_now=True)
    created_time = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name = verbose_name_plural = "项目"

class ServerList(models.Model):
    SERVERLIST_YESORNO = (
        (0, '是'),
        (1, '否'),
    )

    custom_id = models.CharField(max_length=200, verbose_name="ID")
    created_time = models.DateTimeField(auto_now_add=False, verbose_name="服务器开服时间")
    project = models.ForeignKey(Project, verbose_name="项目名称")
    game_district = models.CharField(max_length=200, verbose_name="游戏大区")
    serice_group_nickname = models.CharField(max_length=200, verbose_name="服务器组别名")
    system_name = models.CharField(max_length=200, verbose_name="系统组命名")
    aid = models.CharField(max_length=200, verbose_name="Aid")
    zone = models.CharField(max_length=200, verbose_name="zone")
    group_name = models.CharField(max_length=200, verbose_name="Groupname")
    unique = models.IntegerField(choices=SERVERLIST_YESORNO, verbose_name="是否唯一")
    pay = models.IntegerField(choices=SERVERLIST_YESORNO, verbose_name="是否开充值")
    # = models.IntegerField(choices=SERVERLIST_YESORNO, verbose_name="是否")

    def __unicode__(self):
        return '[%s][%s]' % (self.custom_id, self.project)

    class Meta:
        verbose_name = verbose_name_plural = "服务器组列表"

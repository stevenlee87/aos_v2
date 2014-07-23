# coding:utf-8
from __future__ import unicode_literals

from django.db import models


class Group(models.Model):
    name = models.CharField(max_length=200, verbose_name="名称")

    update_time = models.DateTimeField(auto_now=True)
    created_time = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name = verbose_name_plural = "主机组"


class Host(models.Model):
    HOST_STATUS = (
        (0, '未使用'),
        (1, '已使用'),
        (2, '其他'),
    )
    name = models.CharField(max_length=200, verbose_name="主机名")
    ip = models.IPAddressField()
    status = models.IntegerField(choices=HOST_STATUS, verbose_name="状态")
    note = models.CharField(max_length=1000, verbose_name="备注")

    group = models.ForeignKey(Group)

    update_time = models.DateTimeField(auto_now=True)
    created_time = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return '<%s:%s:%s>' % (self.name, self.ip, self.status)

    class Meta:
        verbose_name = verbose_name_plural = "主机"

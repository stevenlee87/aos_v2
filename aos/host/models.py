# coding:utf-8
from __future__ import unicode_literals

from django.db import models


class Service(models.Model):
    name = models.CharField(max_length=200, verbose_name="业务名称")

    update_time = models.DateTimeField(auto_now=True)
    created_time = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name = verbose_name_plural = "业务组"


class Host(models.Model):
    HOST_STATUS = (
		(0, '在线'),
        (1, '测试'),
        (2, '空闲'),
        (3, '其他'),
		(4, '宿主机'),
    )
    name = models.CharField(max_length=200, verbose_name="主机名")
    ip_in = models.IPAddressField(verbose_name="内网IP")
    ip_out = models.IPAddressField(blank=True, verbose_name="公网IP")
    status = models.IntegerField(choices=HOST_STATUS, verbose_name="状态")
    comment = models.CharField(max_length=1000, verbose_name="备注")

    service = models.ForeignKey(Service)

    update_time = models.DateTimeField(auto_now=True)
    created_time = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return '<%s:%s:%s>' % (self.name, self.ip_in, self.status)

    class Meta:
        verbose_name = verbose_name_plural = "主机"

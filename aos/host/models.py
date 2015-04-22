# coding:utf-8
from __future__ import unicode_literals

from django.db import models


class Service(models.Model):
    """ 业务框架管理"""
    name = models.CharField(max_length=200, verbose_name="业务名称")
    master_coder = models.CharField(max_length=200, verbose_name="主程")
    customer_service = models.CharField(max_length=200, verbose_name="客服接口人")
    operation = models.CharField(max_length=200, verbose_name="营运接口人")
    test_principal = models.CharField(max_length=200, verbose_name="测试接口人")

    update_time = models.DateTimeField(auto_now=True)
    created_time = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name = verbose_name_plural = "业务"

class CloudAndService(models.Model):
    """云与服务管理"""
    name = models.CharField(max_length=200, verbose_name="云服务名称")
    idc_contact = models.CharField(max_length=200, verbose_name="机房联系人")
    idc_district = models.CharField(max_length=200, verbose_name="机房区域")
    comment = models.CharField(blank=True, max_length=1000, verbose_name="备注")
    update_time = models.DateTimeField(auto_now=True)
    created_time = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name = verbose_name_plural = "云服务名称"

class Host(models.Model):
    """主机管理"""

    HOST_STATUS = (
		(0, '在线'),
        (1, '测试'),
        (2, '空闲'),
        (3, '其他'),
    )

    HOST_TYPE = (
        (0, '虚拟机'),
        (1, '宿主机'),
        (2, '物理机'),
    )

    HOST_MODEL = (
        (0, 'DELL 630'),
        (1, 'DELL 730XD'),
        (2, 'other'),
    )

    HOST_IMAGE = (
        (0, 'centos_6.6_x86_64'),
        (1, 'redhat_6.6_x86_64'),
        (2, 'Windows Server 2008 R2 Datacenter 64位英文版'),
    )

    name = models.CharField(blank=True, max_length=200, verbose_name="主机名")
    ip_in = models.IPAddressField(verbose_name="内网IP")
    ip_out = models.IPAddressField(blank=True, verbose_name="公网IP")
    cpu = models.CharField(blank=True, max_length=200, verbose_name="CPU信息")
    memory = models.CharField(blank=True, max_length=200, verbose_name="内存信息") 
    disk = models.CharField(blank=True, max_length=200, verbose_name="硬盘信息")
    raid = models.CharField(blank=True, max_length=200, verbose_name="raid卡信息")
    drac = models.CharField(blank=True, max_length=200, verbose_name="drac信息")
    service_tag = models.CharField(blank=True, max_length=200, verbose_name="服务标签")
    model = models.IntegerField(choices=HOST_MODEL, verbose_name="主机型号")
    image = models.IntegerField(choices=HOST_IMAGE, verbose_name="主机镜像")
    created_time = models.DateTimeField(blank=True, auto_now_add=False, verbose_name="创建时间")
    expire_time = models.DateTimeField(blank=True, auto_now=False, verbose_name="到期时间")

    service = models.ForeignKey(Service, verbose_name="业务")

    type = models.IntegerField(choices=HOST_TYPE, verbose_name="主机类型")
    status = models.IntegerField(choices=HOST_STATUS, verbose_name="主机状态")

    cloudandservice = models.ForeignKey(CloudAndService, verbose_name="云服务名称", blank=True)

    #comment = models.CharField(blank=True, max_length=1000, verbose_name="备注")
    #comment = models.ForeignKey(HostComment, verbose_name="备注")

    #update_time = models.DateTimeField(blank=True, auto_now=True)
    #created_time = models.DateTimeField(blank=True, auto_now_add=True)

    def __unicode__(self):
        return '[%s][%s]' % (self.name, self.ip_in)

    class Meta:
        verbose_name = verbose_name_plural = "主机"

#class HostComment(models.Model):
#    """主机备注"""
#    #comment = models.CharField(blank=True, max_length=1000, verbose_name="备注")
#    host = models.ForeignKey(Host, verbose_name="主机")
#    comment = models.CharField(blank=True, max_length=1000, verbose_name="备注")
#    update_time = models.DateTimeField(auto_now=True)
#    created_time = models.DateTimeField(auto_now_add=True)
#
#    def __unicode__(self):
#        #return '[%s] [%s]' % (self.comment, self.update_time.strftime('%Y-%m-%d %H:%M:%S'))
#        return '[%s]' % self.comment
#
#    class Meta:
#        verbose_name = verbose_name_plural = "备注"

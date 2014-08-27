# coding: utf-8
from __future__ import unicode_literals
import os
from optparse import OptionParser

from django.core.management.base import BaseCommand, CommandError
from host.models import Host, Service, InternetDataCenter, HostComment

parser = OptionParser() 
status_desc_all = ''
service_desc_all = '' 
i = 1

for status_desc in Host.HOST_STATUS:
    status_desc_all +=  "status_id:%d-%s " % (status_desc[0], status_desc[1])

#for service_desc in Service.objects.filter(id__in=Host.objects.values_list('service').distinct()).values_list('name', flat=True):
for service_desc in Service.objects.all():
    service_desc_all +=  "service_id:%d-%s " % (i, service_desc)
    i += 1

class Command(BaseCommand):
    #option_list = BaseCommand.option_list + (
    option_list = (
        parser.add_option(str('-i'), '--ip_in',  action='store', dest='iplist', default=False, type='string', help='可以是一个单独的ip，也可以是一个ip.list文件(一行一个ip)'),
        parser.add_option(str('-s'), '--service',  action='store', dest='service', default=False, type='string', help=service_desc_all),
        parser.add_option(str('-u'), '--status',  action='store', dest='status', default=False, type='string', help=status_desc_all ),
        parser.add_option(str('-c'), '--comment', action='store', dest='comment',default=False, type='string', help='添加备注信息'),
        )

    def handle(self, *args, **options):
        (options, args) = parser.parse_args() 
        file_path = os.path.abspath(options.iplist)
        ip_list = open(file_path)
        for ip in ip_list:
            #print ip,
            #h = Host(name=options.name, ip_in=ip, ip_out=options.ip_out, internetdatacenter_id=options.internetdatacenter, service_id=options.service, type=options.type, status=options.status, comment=options.comment)
            h = Host.objects.get(ip_in=ip)
            h.service_id = options.service
            h.status = options.status
            h.hostcomment_set.create(comment=options.comment)

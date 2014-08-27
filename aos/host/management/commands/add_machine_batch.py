# coding: utf-8
from __future__ import unicode_literals
import os
from optparse import OptionParser

from django.core.management.base import BaseCommand, CommandError
from host.models import Host, Service, InternetDataCenter

usage = "usage: python %prog add_machine_batch --name test123 --ip_in ip.list --ip_out 61.125.32.150 --idc 1 --service 1 --type 0 --status 1 --comment test-test"
#parser = OptionParser() 
idc_all = ''
status_desc_all = ''
service_desc_all = ''
host_type_all = ''
i = 1
d = 1

for idc in InternetDataCenter.objects.all():
    idc_all +=  "idc_id:%d-%s " % (i, idc)
    i += 1
#for service_desc in Service.objects.filter(id__in=Host.objects.values_list('service').distinct()).values_list('name', flat=True):
for service_desc in Service.objects.all():
    service_desc_all +=  "service_id:%d-%s " % (d, service_desc)
    d += 1
for host_type in Host.HOST_TYPE:
    host_type_all +=  "host_type_id:%d-%s " % (host_type[0], host_type[1])
for status_desc in Host.HOST_STATUS:
    status_desc_all +=  "status_id:%d-%s " % (status_desc[0], status_desc[1])

class Command(BaseCommand):
#    option_list = BaseCommand.option_list + (
#    help = "Usage: python manage.py add_machine_batch --name test123 --ip_in ip.list --ip_out 61.125.32.150 --idc 1 --service 1 --type 0 --status 1 --comment test-test"
    help = "Usage: python manage.py add_machine_batch --name test123 --ip_in ip.list --idc 1 --service 1 --type 0 --status 1 --comment test-test"
    parser = OptionParser(usage = usage)
    option_list = (
        parser.add_option(str('-n'), '--name',   action='store', dest='name',  default=False, type='string', help='add hostname'),
        parser.add_option(str('-i'), '--ip_in',  action='store', dest='iplist', default=False, type='string', help='一个ip.list文件(一行一个ip)'),
#        parser.add_option(str('-o'), '--ip_out', action='store', dest='ip_out',default=False, type='string', help='add host public ip'),
        parser.add_option(str('-d'), '--idc',    action='store', dest='internetdatacenter',  default=False, type='string', help=idc_all),
        parser.add_option(str('-s'), '--service',  action='store', dest='service', default=False, type='string', help=service_desc_all),
        parser.add_option(str('-t'), '--type', action='store', dest='type',default=False, type='string', help=host_type_all),
        parser.add_option(str('-u'), '--status',  action='store', dest='status', default=False, type='string', help=status_desc_all),
        parser.add_option(str('-c'), '--comment', action='store', dest='comment',default=False, type='string', help='添加备注信息'),
        )

    def handle(self, *args, **options):
        (options, args) = parser.parse_args() 
        file_path = os.path.abspath(options.iplist)
        ip_list = open(file_path)
        for ip in ip_list:
#print ip,
#h = Host(name=options.name, ip_in=ip, ip_out=options.ip_out, internetdatacenter_id=options.internetdatacenter, service_id=options.service, type=options.type, status=options.status)
            h = Host(name=options.name, ip_in=ip, ip_out=options.ip_out, internetdatacenter_id=options.internetdatacenter, service_id=options.service, type=options.type, status=options.status)
            h.save()     
            h.hostcomment_set.create(comment=options.comment)


from optparse import OptionParser

from django.core.management.base import BaseCommand, CommandError
from host.models import Host, Service, InternetDataCenter

parser = OptionParser() 

class Command(BaseCommand):
    option_list = BaseCommand.option_list + (
        parser.add_option('-n', '--name',   action='store', dest='name',  default=False, type='string', help='add hostname'),
        parser.add_option('-i', '--ip_in',  action='store', dest='ip_in', default=False, type='string', help='add private ip'),
        parser.add_option('-o', '--ip_out', action='store', dest='ip_out',default=False, type='string', help='add public ip'),
        parser.add_option('-d', '--idc',    action='store', dest='internetdatacenter',  default=False, type='string', help='add hostname'),
        parser.add_option('-s', '--service',  action='store', dest='service', default=False, type='string', help='add private ip'),
        parser.add_option('-t', '--type', action='store', dest='type',default=False, type='string', help='add public ip'),
        parser.add_option('-u', '--status',  action='store', dest='status', default=False, type='string', help='add private ip'),
        parser.add_option('-c', '--comment', action='store', dest='comment',default=False, type='string', help='add public ip'),
        )

    def handle(self, *args, **options):
        (options, args) = parser.parse_args() 
        h = Host(name=options.name, ip_in=options.ip_in, ip_out=options.ip_out, internetdatacenter_id=options.internetdatacenter, service_id=options.service, type=options.type, status=options.status, comment=options.comment)
        h.save()     

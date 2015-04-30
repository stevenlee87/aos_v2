#coding=utf-8

from models import ServerList
from host.models import Host, Service
from django.http import HttpResponse
from django.shortcuts import render_to_response
#from django.utils import simplejson
#import simplejson
#from django.core import serializers
#from django.template import Template, Context

def getAll(request):
    serverlist_list = []
    for serverlist in ServerList.objects.values():
        serverlist_dict = {}
        if serverlist['service_id'] == 2:
            #print serverlist['service_id']
            serverlist_custom_id = serverlist['custom_id']
            #print serverlist_custom_id
            serverlist_server_group_nickname = serverlist['server_group_nickname']
            for service in Service.objects.values():
                if service['id'] == 2:
                    service_custom_id = service['custom_id']
            for host in Host.objects.values():
                if host['id'] == serverlist['host_id']:
                    host_ip_in = host['ip_in']
                    host_ip_out = host['ip_out']
            serverlist_dict['serverlist_custom_id'] = serverlist_custom_id
            serverlist_dict['server_group_nickname'] = serverlist_server_group_nickname
            serverlist_dict['service_custom_id'] =  service_custom_id
            serverlist_dict['host_ip_in'] = host_ip_in
            serverlist_dict['host_ip_out'] = host_ip_out
            #print "serverlist_dict is %s"  % serverlist_dict
            serverlist_list.append(serverlist_dict)
            #print serverlist_list
        else:
            continue
    return render_to_response('servicespecific/server.xml', {'zones': serverlist_list}, content_type="application/xhtml+xml")        
    serverlist_list = []
    #return render_to_response('servicespecific/test.xml', {'zones': ServerList.objects.values()})

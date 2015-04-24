#coding=utf-8

from models import ServerList
from django.http import HttpResponse
from django.shortcuts import render_to_response
#from django.utils import simplejson
import simplejson
from django.core import serializers
from django.template import Template, Context

def getAll(request):
    #data = serializers.serialize("xml", ServerList.objects.all())
    #print data
    #serverlists = ServerList.objects.all()
    #serverlist_dict = []
    #flag_dict = {'Y':True,'N':False}
    #for serverlist in serverlists:
    #    serverlist_dict.append({'custom_id':serverlist.id,'created_time':serverlist.created_time,'project':serverlist.project,'game_district':serverlist.game_district,'serice_group_nickname':serverlist.serice_group_nickname,'system_name':serverlist.system_name,'aid':serverlist.aid,'zone':serverlist.zone,'group_name':serverlist.group_name,'unique':serverlist.unique,'pay':serverlist.pay})
    #return HttpResponse(simplejson.dumps(serverlist_dict), mimetype = 'application/json')
    #return render_to_response('current_datetime.html', )
    #return render_to_response('servicespecific/test.xml', {'zone': '"192.168.1.10"'}, mimetype="application/xml")  
    #serverlist_dict = []
    #for serverlist in ServerList.objects.values():
    #    serverlist_dict.append(serverlist)
    #zoneid = serverlist['zone'].encode('utf-8')
    #print zoneid
    #aid = serverlist['aid'].encode('utf-8')
    #return render_to_response('servicespecific/test.xml', {'zone': zoneid, 'aid': aid})
    #return render_to_response('servicespecific/test.xml', {'serverlist_dict_list': serverlist_dict })
    host_dict = []
    #for host in Host.objects.values():
        
    return render_to_response('servicespecific/test.xml', {'zones': ServerList.objects.values()})

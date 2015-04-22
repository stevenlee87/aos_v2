#coding=utf-8

from models import ServerList
from django.http import HttpResponse
from django.shortcuts import render_to_response
#from django.utils import simplejson
import simplejson
from django.core import serializers

def getAll(request):
    #data = serializers.serialize("xml", ServerList.objects.all())
    #print data
    serverlists = ServerList.objects.all()
    serverlist_dict = []
    #flag_dict = {'Y':True,'N':False}
    for serverlist in serverlists:
        serverlist_dict.append({'custom_id':serverlist.id,'created_time':serverlist.created_time,'project':serverlist.project,'game_district':serverlist.game_district,'serice_group_nickname':serverlist.serice_group_nickname,'system_name':serverlist.system_name,'aid':serverlist.aid,'zone':serverlist.zone,'group_name':serverlist.group_name,'unique':serverlist.unique,'pay':serverlist.pay})
    #return HttpResponse(simplejson.dumps(serverlist_dict), mimetype = 'application/json')
    #return render_to_response('current_datetime.html', )
    return render_to_response('servicespecific/servicespecific.xml', {'custom_id': serverlist_dict.custom_id}, mimetype="application/xml")  

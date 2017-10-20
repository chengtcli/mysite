# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from models import Obj
from django.http.response import HttpResponseRedirect

def index(request):
    objs = Obj.objects.all()
    return render(request, 'obj/index.html', {'objs': objs})

def detail(request, oid):
    obj = Obj.objects.get(pk=oid)
    props = ('name', 'id', 'created_at', 'last_update', 'is_pubic')
    return render(request, 'obj/detail.html', {'obj': obj, 'props': props})

def new(request):
    return render(request, 'obj/new.html')

def do_create(request):
    name = request.POST['name']
    is_public = request.POST['is_public'] if 'is_public' in request.POST else False
    new_obj = Obj(name=name, is_public=is_public)
    new_obj.save()
    return HttpResponseRedirect('/obj/{}'.format(new_obj.id))

def delete(request):
    pass
#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
  @author   : Mrhjx0
  @license  : (C) Copyright 2013-2019, Node Supply Chain Manager Corporation Limited.
  @contact  : mrhjx2@gmail.com
  @file     : views_role.py
  @time     : 2019/1/18 16:39
  @desc     :
"""
from django.views.generic import TemplateView
from django.views.generic.base import View
from django.shortcuts import HttpResponse
import json
from .mixin import LoginRequiredMixin
from .models import Role
from apps.custom import RbacCreateView, RbacUpdateView


class RoleView(LoginRequiredMixin, TemplateView):

    template_name = 'system/role.html'


class RoleCreateView(RbacCreateView):
    model = Role
    fields = '__all__'


class RoleListView(LoginRequiredMixin, View):

    def get(self, request):
        fields = ['id', 'name', 'desc']
        ret = dict(data=list(Role.objects.values(*fields)))
        return HttpResponse(json.dumps(ret), content_type='application/json')


class RoleUpdateView(RbacUpdateView):
    model = Role
    fields = '__all__'
    template_name_suffix = '_update'


class RoleDeleteView(LoginRequiredMixin, View):
    def post(self, request):
        ret = dict(result=False)
        if 'id' in request.POST and request.POST['id']:
            id_list = map(int, request.POST['id'].split(','))
            Role.objects.filter(id__in=id_list).delete()
            ret['result'] = True
        return HttpResponse(json.dumps(ret), content_type='application/json')

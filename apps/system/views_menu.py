#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
  @author   : Mrhjx0
  @license  : (C) Copyright 2013-2019, Node Supply Chain Manager Corporation Limited.
  @contact  : mrhjx2@gmail.com
  @file     : view_menu.py
  @time     : 2019/1/17 17:46
  @desc     :
"""

import json

# from django.views.generic.base import View
from django.views.generic import ListView, UpdateView
# from django.shortcuts import render
from django.shortcuts import HttpResponse
from django.http import Http404

from .mixin import LoginRequiredMixin
# from apps.custom import SimpleInfoCreateView
from .models import Menu
from apps.custom import RbacCreateView, RbacUpdateView
# from .forms import MenuForm


# class MenuCreateView(LoginRequiredMixin, View):
#
#     def get(self, request):
#         ret =dict(menu_all=Menu.objects.all())
#         return render(request, 'system/rbac/menu_create.html', ret)
#
#     def post(self, request):
#         res = dict(result=False)
#         menu = Menu()
#         menu_form = MenuForm(request.POST, instance=menu)
#         if menu_form.is_valid():
#             menu_form.save()
#             res['result'] = True
#         return HttpResponse(json.dumps(res), content_type='application/json')
    # 最后配置URL和模板页，菜单的填加功能就完成了。 比较常用的添加视图的写法

# class MenuCreateView(LoginRequiredMixin, CreateView):
#     model = Menu
#     fields = '__all__'
#     # success_url = 'system/rbac/menu/create'
#
#     def post(self, request, *args, **kwargs):
#         res = dict(result=False)
#         form = self.get_form()
#         if form.is_valid():
#             form.save()
#             res['result'] = True
#         return HttpResponse(json.dumps(res), content_type='application/json')

# class MenuCreateView(SimpleInfoCreateView):
#     model = Menu
#     fields = '__all__'
#     extra_context = dict(menu_all=Menu.objects.all())
class MenuCreateView(RbacCreateView):
    model = Menu
    fields = '__all__'
    # extra_context = dict(menu_all=Menu.objects.all())
    def get_context_data(self, **kwargs):
        kwargs['menu_all'] = Menu.objects.all()
        return super().get_context_data(**kwargs)


class MenuListView(LoginRequiredMixin, ListView):
    model = Menu
    context_object_name = 'menu_all'


# class MenuUpdateView(LoginRequiredMixin, UpdateView):
#     model = Menu
#     fields = '__all__'
#     template_name_suffix = '_update'
#     # success_url = 'system/rbac/menu/'
#     extra_context = dict(menu_all=Menu.objects.all())
#
#     def get_object(self, queryset=None):
#
#         if queryset is None:
#             queryset = self.get_queryset()
#         if 'id' in self.request.GET and self.request.GET['id']:
#             queryset = queryset.filter(id=int(self.request.GET['id']))
#         elif 'id' in self.request.POST and self.request.POST['id']:
#             queryset = queryset.filter(id=int(self.request.POST['id']))
#         else:
#             raise AttributeError("Generic detail view %s must be called with id. "
#                                  % self.__class__.__name__)
#         try:
#             obj = queryset.get()
#         except queryset.model.DoesNotExist:
#             raise Http404("No %(verbose_name)s found matching the query" %
#                           {'verbose_name': queryset.model._meta.verbose_name})
#         return obj
#
#     def post(self, request, *args, **kwargs):
#
#         self.object = self.get_object()
#         res = dict(result=False)
#         form = self.get_form()
#         if form.is_valid():
#             form.save()
#             res['result'] = True
#         return HttpResponse(json.dumps(res), content_type='application/json')
class MenuUpdateView(RbacUpdateView):
    model = Menu
    fields = '__all__'
    template_name_suffix = '_update'
    # extra_context = dict(menu_all=Menu.objects.all())

    def get_context_data(self, **kwargs):
        kwargs['menu_all'] = Menu.objects.all()
        return super().get_context_data(**kwargs)

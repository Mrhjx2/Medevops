#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
  @author   : Mrhjx0
  @license  : (C) Copyright 2013-2019, Node Supply Chain Manager Corporation Limited.
  @contact  : mrhjx2@gmail.com
  @file     : custom.py
  @time     : 2019/1/18 9:42
  @desc     :
"""

import json
from django.views.generic import CreateView, UpdateView
from django.shortcuts import HttpResponse
from django.http import Http404
from .system.mixin import LoginRequiredMixin


# class SimpleInfoCreateView(LoginRequiredMixin, CreateView):
#
#     def post(self, request, *args, **kwargs):
#         res = dict(result=False)
#         form = self.get_form()
#
#         if form.is_valid():
#             # print(form)
#             form.save()
#             res['result'] = True
#         return HttpResponse(json.dumps(res), content_type='application/json')
#
#
# class RbacUpdateView(LoginRequiredMixin, UpdateView):
#
#     def post(self, request, *args, **kwargs):
#         self.object = self.get_object()
#         res = dict(result=False)
#         form = self.get_form()
#         if form.is_valid():
#             form.save()
#             res['result'] = True
#         return HttpResponse(json.dumps(res), content_type='application/json')


class RbacEditViewMixin:

    def post(self, reuest, *args, **kwargs):
        res = dict(result=False)
        form = self.get_form()
        if form.is_valid():
            form.save()
            res['result'] = True

        return HttpResponse(json.dumps(res), content_type='application/json')


class RbacCreateView(LoginRequiredMixin, RbacEditViewMixin, CreateView):
    """
    View for create an object, with a response rendered by a template.
    Returns information with Json when the data is create successfully or fails.
    """


class RbacGetObjectMixin:
    def get_object(self, queryset=None):

        if queryset is None:
            queryset = self.get_queryset()
            if 'id' in self.request.GET and self.request.GET['id']:
                queryset = queryset.filter(id=int(self.request.GET['id']))
            elif 'id' in self.request.POST and self.request.POST['id']:
                queryset = queryset.filter(id=int(self.request.POST['id']))
            else:
                raise AttributeError("Generic detail view %s must be called with id. " %
                                     self.__class__.__name__)
            try:
                obj = queryset.get()
            except queryset.model.DoesNotExist:
                raise Http404("No %(verbose_name)s found matching the query" %
                              {'verbose_name': queryset.model_meta.verbose_name})

            return obj


class RbacUpdateView(LoginRequiredMixin, RbacEditViewMixin, RbacGetObjectMixin, UpdateView):

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        return super().post(request, *args, **kwargs)

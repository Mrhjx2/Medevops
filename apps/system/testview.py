#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
  @author   : Mrhjx0
  @license  : (C) Copyright 2013-2019, Node Supply Chain Manager Corporation Limited.
  @contact  : mrhjx2@gmail.com
  @file     : testview.py
  @time     : 2019/1/17 15:29
  @desc     :
"""
# from django.views.generic.base import View, TemplateView
from django.views.generic import ListView
# from django.template.response import TemplateResponse
from django.contrib.auth import get_user_model
from .models import Structure

User = get_user_model()

# class TestView(View):
#
#     def get(self,request):
#         ret = dict(user_all=User.objects.all())
#         return TemplateResponse(request, 'system/testview.html', ret)


# class TestView(TemplateView):
#
#     template_name = 'system/testview.html'
#     extra_context = dict(user_all=User.objects.all())


class TestView(ListView):
    template_name = 'system/testview.html'
    model = User
    context_object_name = 'user_all'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(TestView, self).get_context_data(**kwargs)
        context['structure_all'] = Structure.objects.all()
        return context

    def get_queryset(self):
        return User.objects.filter(gender=self.kwargs['gender'])

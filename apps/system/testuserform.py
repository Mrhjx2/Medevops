#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
  @author   : Mrhjx0
  @license  : (C) Copyright 2013-2019, Node Supply Chain Manager Corporation Limited.
  @contact  : mrhjx2@gmail.com
  @file     : testuserform.py
  @time     : 2019/1/11 17:46
  @desc     :
"""
from django.shortcuts import render, HttpResponseRedirect
from django.views.generic.base import View
from .forms import UserTestForm


class FormTestView(View):

    def get(self, request):
        test_form = UserTestForm()
        return render(request, 'system/users/form_test.html', {'test_form': test_form})

    def post(self, request):
        test_form = UserTestForm(request.POST)
        ret = dict(test_form=test_form)
        ret['errors'] = test_form.errors.as_json()
        if test_form.is_valid():
            # form验证通过后，重定向到项目首页，由于项目IndexView限制登录访问了，如果系统没登录这个重定向先跳到登录页面
            # 过form.cleaned_data获取通过表单验证的数据
            username = test_form.cleaned_data['username']
            password = test_form.cleaned_data['password']
            # 依然可以通过request.POST来获取数据
            username1 = request.POST['username']
            return HttpResponseRedirect('/')

        return render(request, 'system/users/form_test.html', ret)

#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
  @author   : Mrhjx0
  @license  : (C) Copyright 2013-2019, Node Supply Chain Manager Corporation Limited.
  @contact  : mrhjx2@gmail.com
  @file     : views_create.py.py
  @time     : 2019/1/17 17:57
  @desc     :
"""

from django.views.generic import CreateView

from .mixin import LoginRequiredMixin
from .models import Menu

class MenuCreateView(LoginRequiredMixin, CreateView):
    model = Menu
    fields = '__all__'
    success_url = '/system/rbac/menu/create'

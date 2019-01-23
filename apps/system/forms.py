#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
  @author   : Mrhjx0
  @license  : (C) Copyright 2013-2019, Node Supply Chain Manager Corporation Limited.
  @contact  : mrhjx2@gmail.com
  @file     : forms.py
  @time     : 2019/1/10 14:44
  @desc     :
"""
from django import forms
from system.models import Structure, Menu
import re
from django.contrib.auth import get_user_model

User = get_user_model()


class LoginForm(forms.Form):
    username = forms.CharField(required=True, error_messages={"requeired": "请填写用户名"})
    password = forms.CharField(required=True, error_messages={"requeired": "请填写密码"})


class StructureForm(forms.ModelForm):
    class Meta:
        model = Structure
        fields = ['type', 'name', 'parent']


class UserTestForm(forms.Form):
    username = forms.CharField(label='用户名', max_length=10)
    password = forms.CharField(label='密码', max_length=10)


class UserCreateForm(forms.ModelForm):
    """
    在添加用户时，我们需要对输入的数据进行有效性验证，包括：密码长度和有效性验证、关键字段的有效性验证、
    用户名重复性验证、手机号码有效性验证、手机号码重复性验证等等，同时还要对错误输入提供有效的错误提示信息，看
    起来要求很多，不过好在django表单功能提供了各种验证方法。
    知识点：
    1、error_messages：表单字段的关键参数，通过覆盖字段引发的异常中的默认信息，实现自定义错误提示信息。
    2、clean()方法：重写clean()方法可以实现额外的验证功能。
    3、ValidationError：当form验证的数据有问题都会引发ValidationError，并将相关的错误信息传递给
    ValidationError，项目中通过重写clean()方法对输入的数据进行额外验证，不合规的数据输入将会触发ValidationError，返回错误信息。
    """
    password = forms.CharField(
        required=True,
        min_length=6,
        max_length=20,
        error_messages={
            "required": "密码不能为空",
            "min_length": "密码长度最少6位数",
        }
    )

    confirm_password = forms.CharField(
        required=True,
        min_length=6,
        max_length=20,
        error_messages={
            "required": "确认密码不能为空",
            "min_length": "密码长度最少6位数",
        }
    )

    class Meta:
        model = User
        fields = [
            'name', 'gender', 'birthday', 'username', 'mobile', 'email',
            'department', 'post', 'superior', 'is_active', 'roles', 'password'
        ]

        error_messages = {
            "name": {"required": "姓名不能为空"},
            "username": {"required": "用户名不能为空"},
            "email": {"required": "邮箱不能为空"},
            "mobile": {
                "required": "手机号码不能为空",
                "max_length": "输入有效的手机号码",
                "min_length": "输入有效的手机号码",
            },
        }

    def clean(self):
        cleaned_data = super(UserCreateForm, self).clean()
        username = cleaned_data.get("username")
        mobile = cleaned_data.get("mobile", "")
        email = cleaned_data.get("email")
        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("confirm_password")

        if User.objects.filter(username=username).count():
            raise forms.ValidationError('用户名：{}已存在'.format(username))

        if password != confirm_password:
            raise forms.ValidationError("两次密码输入不一致")

        if User.objects.filter(mobile=mobile).count():
            raise forms.ValidationError('手机号码: {} 已存在'.format(mobile))

        REGEX_MOBILE = "^1[3578]\d{9}$|^147\d{8}$|^176\d{8}$"
        if not re.match(REGEX_MOBILE, mobile):
            raise forms.ValidationError("手机号码非法")

        if User.objects.filter(email=email).count():
            raise forms.ValidationError('邮箱：{}已存在'.format(email))


class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = [
            'name', 'gender', 'birthday', 'username', 'mobile', 'email',
            'department', 'post', 'superior', 'is_active', 'roles'
        ]


class PasswordchangeForm(forms.Form):

    password = forms.CharField(
        required=True,
        min_length=6,
        max_length=20,
        error_messages={
            "required": u"密码不能为空"
        }
    )

    confirm_password = forms.CharField(
        required=True,
        min_length=6,
        max_length=20,
        error_messages={
            "required": u"确认密码不能为空"
        }
    )

    def clean(self):
        clean_data = super(PasswordchangeForm, self).clean()
        password = clean_data.get("password")
        confirm_password = clean_data.get("confirm_password")
        if password != confirm_password:
            raise forms.ValidationError("两次密码输入不一致")


class MenuForm(forms.ModelForm):
    class Meta:
        model = Menu
        fields = '__all__'

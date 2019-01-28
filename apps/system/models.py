# -*- coding: utf-8 -*-
# system models
# 2019-01-04 by mrhjx0

from django.db import models
from django.contrib.auth.models import AbstractUser
# from django.utils.translation import gettext_lazy as _
# Create your models here.


class Menu(models.Model):
    """
    菜单
    """
    name = models.CharField(max_length=30, unique=True, verbose_name="菜单名")  # unique = True,这个字段在表中必须有唯一值，
    parent = models.ForeignKey("self", null=True, blank=True, on_delete=models.SET_NULL, verbose_name="父菜单")
    icon = models.CharField(max_length=50, null=True, blank=True, verbose_name="图标")
    code = models.CharField(max_length=50, null=True, blank=True, verbose_name="编码")
    url = models.CharField(max_length=128, unique=True, null=True, blank=True)
    number = models.FloatField(null=True, blank=True,verbose_name="编号")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = '菜单'
        verbose_name_plural = verbose_name
        ordering = ['number']
        # abstract = True

    @classmethod
    def get_menu_by_request_url(cls, url):
        try:
            return dict(menu=Menu.objects.get(url=url))
        except:
            return None


class Role(models.Model):
    """
    角色：用于权限绑定
    """
    name = models.CharField(max_length=32, unique=True, verbose_name="角色")
    permissions = models.ManyToManyField("Menu", blank=True, verbose_name="URL授权")
    desc = models.CharField(max_length=50, blank=True, null=True, verbose_name="描述")

    class Meta:
        verbose_name = '角色'
        verbose_name_plural = verbose_name
        # abstract = True


class Structure(models.Model):
    """
    组织架构 组织架构主要是权限管理模块中人员的层级架构，可以是公司的组织结构、部分、小组等。
    """
    type_choices = (("unit", "单位"), ("department", "部门"))
    name = models.CharField(max_length=60, verbose_name="名称")
    type = models.CharField(max_length=20, choices=type_choices, default="department",
                            verbose_name="类型")
    parent = models.ForeignKey("self", null=True, blank=True, on_delete=models.SET_NULL,
                               verbose_name="父类架构")

    class Meta:
        verbose_name = "组织架构"
        verbose_name_plural = verbose_name
        # abstract = True

    def __str__(self):
        return self.name


class UserProfile(AbstractUser):
    """
    User model
    """
    name = models.CharField(max_length=20, default="", verbose_name="姓名")
    birthday = models.DateField(null=True, blank=True, verbose_name="出生日期")
    gender = models.CharField(max_length=10, choices=(("male", "男"), ("female", "女")),
                              default="male", verbose_name="性别")
    mobile = models.CharField(max_length=14, default="", verbose_name="手机号码")
    # email = models.EmailField(max_length=32, verbose_name="邮箱")
    image = models.ImageField(upload_to="image/%Y/%m", default="image/default.jpg",
                              max_length=100, null=True, blank=True)
    department = models.ForeignKey("Structure", null=True, blank=True, on_delete=models.SET_NULL,
                                   verbose_name="部门")
    post = models.CharField(max_length=50, null=True, blank=True, verbose_name="职位")
    superior = models.ForeignKey("self", null=True, blank=True, on_delete=models.SET_NULL, verbose_name="上级主管")
    roles = models.ManyToManyField("Role", verbose_name="角色", blank=True)

    # class Meta:
    #     verbose_name = _('user')
    #     verbose_name_plural = _('users')
    #     abstract = True

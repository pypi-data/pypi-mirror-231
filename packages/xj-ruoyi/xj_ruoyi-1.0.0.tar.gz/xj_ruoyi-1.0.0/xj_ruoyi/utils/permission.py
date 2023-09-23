import re

from django.contrib.auth.models import AnonymousUser
from django.db.models import F
from rest_framework.permissions import BasePermission

from ..models import ApiWhiteList


def ValidationApi(reqApi, validApi):
    """
    验证当前用户是否有接口权限
    :param reqApi: 当前请求的接口
    :param validApi: 用于验证的接口
    :return: True或者False
    """
    if validApi is not None:
        valid_api = validApi.replace('{id}', '.*?')
        matchObj = re.match(valid_api, reqApi, re.M | re.I)
        if matchObj:
            return True
        else:
            return False
    else:
        return False


class AnonymousUserPermission(BasePermission):
    """
    匿名用户权限
    """

    def has_permission(self, request, view):
        if isinstance(request.user, AnonymousUser):
            return False
        return True


def ReUUID(api):
    """
    将接口的uuid替换掉
    :param api:
    :return:
    """
    pattern = re.compile(r'[a-f\d]{4}(?:[a-f\d]{4}-){4}[a-f\d]{12}/$')
    m = pattern.search(api)
    if m:
        res = api.replace(m.group(0), ".*/")
        return res
    else:
        return None


class CustomPermission(BasePermission):
    """自定义权限"""

    def has_permission(self, request, view):
        if isinstance(request.user, AnonymousUser):
            return False
        # 判断是否是超级管理员
        if request.user.is_superuser:
            return True
        else:
            api = request.path  # 当前请求接口
            method = request.method  # 当前请求方法
            methodList = ['GET', 'POST', 'PUT', 'DELETE', 'OPTIONS', 'PATCH']
            userApiList = request.user.role.values('api_white__url', 'api_white__method')  # 获取当前用户的角色拥有的所有接口
            # 检查 QuerySet 中每个对象的字段是否均为 None
            is_empty = all(item['api_white__url'] is None and item['api_white__method'] is None for item in userApiList)
            if is_empty:
                return False
            ApiList = [
                str(item.get('api_white__url').replace('{id}', '([a-zA-Z0-9-]+)')) for item in userApiList if
                item.get('api_white__url')]
            if api in ApiList:
                return True
            else:
                return False


class SuperuserPermission(BasePermission):
    """
    超级管理员权限类
    """

    def has_permission(self, request, view):
        if isinstance(request.user, AnonymousUser):
            return False
        # 判断是否是超级管理员
        if request.user.is_superuser:
            return True


class AdminPermission(BasePermission):
    """
    普通管理员权限类
    """

    def has_permission(self, request, view):
        if isinstance(request.user, AnonymousUser):
            return False
        # 判断是否是超级管理员
        is_superuser = request.user.is_superuser
        # 判断是否是管理员角色
        is_admin = request.user.role.values_list('admin', flat=True)
        if is_superuser or True in is_admin:
            return True

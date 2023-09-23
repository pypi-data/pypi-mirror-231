# -*- coding: utf-8 -*-

"""
@author: 高栋天
@contact: QQ:14995936944
@Created on: 2023/9/13 001 22:57
@Remark: 自定义视图集
"""
import uuid
from django.core.exceptions import FieldError
from django.db.models import fields
from django.db.models import CharField, IntegerField, DateField
from django.db import transaction
from django.db.models import F
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from rest_framework.decorators import action
from rest_framework.viewsets import ModelViewSet
from .custom_jwt_auth import CustomJWTAuthentication
from ..utils.filters import DataLevelPermissionsFilter
from ..utils.import_export_mixin import ExportSerializerMixin, ImportSerializerMixin
from ..utils.json_response import SuccessResponse, ErrorResponse, DetailResponse
from ..utils.permission import CustomPermission
from django_restql.mixins import QueryArgumentsMixin
from rest_framework.pagination import PageNumberPagination


class MyPageNumberPagination(PageNumberPagination):
    # 每页显示多少个
    page_size = 10
    # 默认每页显示3个，可以通过传入pager1/?page=2&size=4,改变默认每页显示的个数
    page_size_query_param = "size"
    # 最大页数不超过10
    max_page_size = 10
    # 获取页码数的
    page_query_param = "page"


class CustomModelViewSet(ModelViewSet, ImportSerializerMixin, ExportSerializerMixin, QueryArgumentsMixin):
    authentication_classes = [CustomJWTAuthentication]

    def check_permissions(self, request):
        pass  # 无需执行任何权限检查
    """
    自定义的ModelViewSet:
    统一标准的返回格式;新增,查询,修改可使用不同序列化器
    (1)ORM性能优化, 尽可能使用values_queryset形式
    (2)xxx_serializer_class 某个方法下使用的序列化器(xxx=create|update|list|retrieve|destroy)
    (3)filter_fields = '__all__' 默认支持全部model中的字段查询(除json字段外)
    (4)import_field_dict={} 导入时的字段字典 {model值: model的label}
    (5)export_field_label = [] 导出时的字段
    """
    values_queryset = None
    ordering_fields = '__all__'
    create_serializer_class = None
    update_serializer_class = None
    filter_fields = '__all__'
    search_fields = ()
    extra_filter_backends = [DataLevelPermissionsFilter]
    permission_classes = [CustomPermission]
    import_field_dict = {}
    export_field_label = {}

    # def filter_queryset(self, queryset):
    #     for backend in set(set(self.filter_backends) | set(self.extra_filter_backends or [])):
    #         queryset = backend().filter_queryset(self.request, queryset, self)
    #     return queryset

    def filter_queryset(self, queryset):
        filter_fields = getattr(self, 'filter_fields', None)
        request = self.request
        query_params = request.query_params
        if filter_fields and query_params:
            model = queryset.model
            model_fields = [f.name for f in model._meta.get_fields()]
            for field in filter_fields:
                if field in model_fields:
                    field_object = model._meta.get_field(field)
                    value = query_params.get(field)
                    if value is not None:
                        if isinstance(field_object, fields.CharField):
                            queryset = queryset.filter(**{f"{field}__icontains": value})
                        elif isinstance(field_object, fields.BooleanField):
                            if value.lower() in {'true', '1'}:
                                queryset = queryset.filter(**{field: True})
                            elif value.lower() in {'false', '0'}:
                                queryset = queryset.filter(**{field: False})
                            else:
                                raise FieldError(f"Invalid value for field '{field}'.")
                        elif isinstance(field_object, fields.IntegerField):
                            queryset = queryset.filter(**{field: int(value)})
                        elif isinstance(field_object, fields.FloatField):
                            queryset = queryset.filter(**{field: float(value)})
                        else:
                            queryset = queryset.filter(**{field: value})
        for backend in set(set(self.filter_backends) | set(self.extra_filter_backends or [])):
            queryset = backend().filter_queryset(self.request, queryset, self)
        return queryset

    def get_queryset(self):
        if getattr(self, 'values_queryset', None):
            return self.values_queryset
        return super().get_queryset()

    def get_serializer_class(self):
        action_serializer_name = f"{self.action}_serializer_class"
        action_serializer_class = getattr(self, action_serializer_name, None)
        if action_serializer_class:
            return action_serializer_class
        return super().get_serializer_class()

    # 通过many=True直接改造原有的API，使其可以批量创建
    def get_serializer(self, *args, **kwargs):
        serializer_class = self.get_serializer_class()
        kwargs.setdefault('context', self.get_serializer_context())
        if isinstance(self.request.data, list):
            with transaction.atomic():
                return serializer_class(many=True, *args, **kwargs)
        else:
            return serializer_class(*args, **kwargs)

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data, request=request)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        return DetailResponse(data=serializer.data, msg="新增成功")

    def list(self, request, *args, **kwargs):
        sort = request.query_params.get('sort', '')  # 获取传入的 sort 参数值
        queryset = self.filter_queryset(self.get_queryset())

        if sort:
            if sort.startswith('-'):
                # 倒序排序
                sort_field = sort[1:]  # 去掉前面的负号
                queryset = queryset.order_by(F(sort_field).desc())
            else:
                # 正序排序
                queryset = queryset.order_by(sort)

        pg = MyPageNumberPagination()
        # 获取分页的数据
        page = pg.paginate_queryset(queryset=queryset, request=request, view=self)
        if page is not None:
            total = queryset.count()
            serializer = self.get_serializer(page, many=True, request=request)
            return SuccessResponse(data=serializer.data, msg="获取成功", page=int(request.query_params.get('page', 1)),
                                   size=int(request.query_params.get('size', 1)), total=total)

        serializer = self.get_serializer(queryset, many=True, request=request)
        return SuccessResponse(data=serializer.data, msg="获取成功")

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        return DetailResponse(data=serializer.data, msg="获取成功")

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, request=request, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)

        if getattr(instance, '_prefetched_objects_cache', None):
            # If 'prefetch_related' has been applied to a queryset, we need to
            # forcibly invalidate the prefetch cache on the instance.
            instance._prefetched_objects_cache = {}
        return DetailResponse(data=serializer.data, msg="更新成功")

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.delete()
        return DetailResponse(data=[], msg="删除成功")

    keys = openapi.Schema(description='主键列表', type=openapi.TYPE_ARRAY, items=openapi.TYPE_STRING)

    @swagger_auto_schema(request_body=openapi.Schema(
        type=openapi.TYPE_OBJECT,
        required=['keys'],
        properties={'keys': keys}
    ), operation_summary='批量删除')
    @action(methods=['delete'], detail=False)
    def multiple_delete(self, request, *args, **kwargs):
        request_data = request.data
        keys = request_data.get('keys', None)
        if keys:
            self.get_queryset().filter(id__in=keys).delete()
            return SuccessResponse(data=[], msg="删除成功")
        else:
            return ErrorResponse(msg="未获取到keys字段")

# -*- coding: utf-8 -*-

"""
@author: 高栋天
@contact: QQ:1499593644
@Created on: 2022/1/1 001 9:34
@Remark:
"""
from ..models import Post
from ..utils.serializers import CustomModelSerializer
from ..utils.viewset import CustomModelViewSet


class PostSerializer(CustomModelSerializer):
    """
    岗位-序列化器
    """

    class Meta:
        model = Post
        fields = "__all__"
        read_only_fields = ["id"]


class PostViewSet(CustomModelViewSet):
    """
    岗位表
    list:查询
    create:新增
    update:修改
    retrieve:单例
    destroy:删除
    """
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    filter_fields = ['name', 'code', 'status']

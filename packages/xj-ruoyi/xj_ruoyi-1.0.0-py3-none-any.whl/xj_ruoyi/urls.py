# _*_coding:utf-8_*_

from django.urls import re_path, path
from rest_framework import routers

from .views.api_white_list import ApiWhiteListViewSet
from .views.dept import DeptViewSet
from .views.menu import MenuViewSet
from .views.menu_button import MenuButtonViewSet
from .views.operation_log import OperationLogViewSet
from .views.post import PostViewSet
from .views.role import RoleViewSet

app_name = 'xj_ruoyi'
system_url = routers.SimpleRouter()
system_url.register(r'dept', DeptViewSet)
system_url.register(r'menu', MenuViewSet)
system_url.register(r'role', RoleViewSet)
system_url.register(r'menu_button', MenuButtonViewSet)
system_url.register(r'api_white_list', ApiWhiteListViewSet)
system_url.register(r'operation_log', OperationLogViewSet)
system_url.register(r'post', PostViewSet)

urlpatterns = [
    path('dept_lazy_tree/', DeptViewSet.as_view({'get': 'dept_lazy_tree'})),

]
urlpatterns += system_url.urls

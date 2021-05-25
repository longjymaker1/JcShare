"""
app 路由配置
"""

from django.urls import re_path, path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    # re_path(r"(?<province_id>\d+)$", views.index, name='index')
]




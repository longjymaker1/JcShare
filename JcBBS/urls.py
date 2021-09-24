"""
app 路由配置
"""

# from django.urls import re_path, path
from django.urls import re_path, path
from . import views
from django.conf.urls.static import static
from django.views.generic import TemplateView
from JcShare import settings


urlpatterns = [
    # path('', views.index, name='index'),
    path('', views.IndexView.as_view(template_name="index.html"), name='index'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)




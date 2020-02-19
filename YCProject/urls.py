from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static

from . import settings

urlpatterns = [
    path('admin/', admin.site.urls),
   # 静态资源的路径
] + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)

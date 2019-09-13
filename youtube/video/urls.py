from django.conf import settings
from django.conf.urls.static import static
from django.urls import re_path
from . import views

app_name = 'video'

urlpatterns = [

    re_path(r'upload/$', views.upload, name='upload'),
    re_path(r'download/$', views.download, name='download'),
    re_path(r'play/$', views.play, name='play'),
    re_path(r'test/$', views.test, name='test'),


] + static(settings.MEDIA_URL, document_root= settings.MEDIA_ROOT)


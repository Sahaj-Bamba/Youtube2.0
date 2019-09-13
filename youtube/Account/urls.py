from django.urls import path,re_path

from . import views

app_name = 'Account'

urlpatterns = [

    # re_path(r'^signup/$', views.user_signup, name='signup'),
    # re_path(r'^login/$', views.user_login, name='login'),
    # re_path(r'^logout/$', views.user_logout, name='logout'),
    re_path(r'^profile/$', views.user_profile, name='profile'),

]

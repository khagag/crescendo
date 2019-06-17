from django.urls import path

from . import views

app_name = 'music_blog'
urlpatterns = [
        path('',views.index,name='home'),
        path('login',views.user_login,name='user_login'),
        path('user_panal',views.adminstration,name='admin_panal'),
        path('registration',views.regist,name='regist'),
        path('panal',views.index,name='admin_index'),
        ]

from django.urls import path

from . import views

app_name = 'music_blog'
urlpatterns = [
        path('logout/', views.user_logout, name='logout'),
        path('',views.index,name='index'),
        path('login',views.user_login,name='user_login'),
        path('social',views.social_user_login,name='social_login'),
        path('user_panal',views.adminstration,name='admin_panal'),
        path('registration',views.regist,name='regist'),
        path('panal',views.index,name='admin_index'),
        ]

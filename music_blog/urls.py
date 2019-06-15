from django.urls import path

from . import views

urlpatterns = [
        path('',views.index,name='home'),
        path('panal',views.index,name='admin_index'),
        ]

from django.urls import path

from . import views


app_name='api'
urlpatterns = [
        path('',views.index,name='api'),
        path('music_upload',views.add_song,name='music_add'),
        ]

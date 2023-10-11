from django.contrib import admin
from django.urls import path, re_path
from app.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    re_path(r'^$', ActionView.as_view(), name='home'), #домашняя страница
    re_path(r'^about/(?P<id>\d+)/$', AboutAction.as_view(), name='about'), #страница о задаче, передается pk
    re_path(r'^create', CreateAction.as_view(), name='create'), #страница создания задачи
    re_path(r'^delete/(?P<id>\d+)/$', DeleteAction.as_view(), name='delete') #страница удаления задачи, передается pk
]
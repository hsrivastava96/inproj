from django.contrib import admin
from django.urls import path
from django.conf.urls import url
from django.conf.urls import include
from inpro import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.index, name='index'),
    url(r'^test_data/$', views.test_data, name='test_data'),
    url(r'^excel_Download/$', views.excel_Download, name='excel_Download')
]

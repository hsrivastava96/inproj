from django.contrib import admin
from django.conf.urls import url
from django.conf.urls import include
from inpro import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', include('inpro.urls')),
    url(r'^inpro/', include('inpro.urls')),
]

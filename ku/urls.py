from django.conf.urls import include, url
from django.contrib import admin

from inicio import views

urlpatterns = [
    # url(r'^admin/', include(admin.site.urls)),
    url(r'^$', views.ViewInicio.as_view(), name='inicio'),
    url(r'^inicio/', include("inicio.urls", namespace="inicio"))
]

from django.conf.urls import url

from inicio import views

urlpatterns = [
    url(r'^$', views.ViewInicio.as_view(), name='inicio'),
    url(r'^estres/$', views.ViewEstres.as_view(), name='estres'),
    url(r'^atencion/$', views.ViewAtencion.as_view(), name='atencion'),
    url(r'^deportes/$', views.ViewDeportes.as_view(), name='deportes')
]

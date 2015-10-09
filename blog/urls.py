from django.conf.urls import url
from . import views


urlpatterns = [

     url(r'^$', views.listar_publicaciones),
     url(r'^post/(?P<pk>[0-9]+)/$', views.detalle_publicacion),

]

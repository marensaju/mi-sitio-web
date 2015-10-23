from django.conf.urls import url
from . import views


urlpatterns = [

     url(r'^$', views.listar_publicaciones),
     url(r'^post/(?P<pk>[0-9]+)/$', views.detalle_publicacion),
     url(r'^post/new/$', views.nueva_publicacion, name='nueva_publicacion'),
     url(r'^post/(?P<pk>[0-9]+)/edit/$', views.post_editar, name='post_editar'),

]

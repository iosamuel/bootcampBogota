from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
    url(r'^$', 'principal.views.index'),
    url(r'^insertar/$', 'principal.views.insertar_entrada'),
)

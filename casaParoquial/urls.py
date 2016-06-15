"""casaParoquial URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin
from crud import views
urlpatterns = [
    url(r'^$', views.home),
    url(r'^cadastrar_evento/$', views.cadastrar_evento),
    url(r'^cadastrar_membro/$', views.cadastrar_membro),
    url(r'^consultar_membro/$', views.consulta_membro),
    url(r'^membro/(?P<membro_id>\d+)/$', views.editar_membro),
    url(r'^evento/(?P<evento_id>\d+)/$', views.editar_evento),
    url(r'^consultar_evento/$', views.consultar_evento),
    url(r'^consultar_aconselhamento/$', views.consultar_aconselhamento),
    url(r'^cadastrar_aconselhamento/$', views.cadastrar_aconselhamento),
    url(r'^relatorio_aniversario/$', views.relatorio_aniversario),
    url(r'^consultar_evento_nome/$', views.consultar_evento_nome),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^email/$', views.envia_email),
    url(r'^criandouser1/$', views.login_user1),
    url(r'^criandouser2/$', views.login_user2),
    url(r'^deslog/$', views.deslog),
    url(r'^relatorio_ministerio/$', views.relatorio_ministerio),
    url(r'^relatorio_demografico/$', views.relatorio_demografico),
   
]

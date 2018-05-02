from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^dica1$', views.dica1, name='dica1'),
    url(r'^geral/$', views.geral, name='geral'), 
    url(r'^lista/$', views.cadastro_list, name='cadastro_list'),    
    url(r'^movimentacao/(?P<pk>\d+)/$', views.movimentacao, name='movimentacao'),

    url(r'^talento_list/$', views.talento_list, name='talento_list'),
    url(r'^talento/new/$',	views.talento_crud,	name='talento_crud'),
    url(r'^talento/(?P<pk>\d+)/$',	views.talento_detail,	name='talento_detail'),
    url(r'^talento/(?P<pk>\d+)/edit',  views.talento_edit,   name='talento_edit'),
    
    url(r'^cadastro/new/$',	views.cadastro_crud,	name='cadastro_crud'),
    url(r'^cadastro/(?P<pk>\d+)/$',	views.cadastro_detail,	name='cadastro_detail'),

    url(r'^lancamento/(?P<pk>\d+)/$', views.lancamento_detail, name='lancamento_detail'),
    url(r'^lancamento/new/$',	views.lancamento_new,	name='lancamento_new'),
            
]




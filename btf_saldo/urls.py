
from django.conf.urls import url
from . import views


from btf_saldo.views import NomeAutocomplete


urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^operacao', views.operacao,name='operacao'),    
    url(r'^transferencia', views.transferencia,name='transferencia'),
    url(r'^administrativo', views.administrativo,name='administrativo'),
    url(r'^eventos', views.eventos,name='eventos'),

    url(r'^libera_lista', views.libera_lista, name='libera_lista'),
    url(r'^desbloquear/(?P<pk>\d+)/$', views.desbloquear, name='desbloquear'), 
    url(r'^bloquear/(?P<pk>\d+)/$', views.bloquear, name='bloquear'), 
    url(r'^talentos_filtro', views.talentos_filtro, name='talentos_filtro'), 
    url(r'^talentos/(?P<pk>\d+)/edit2',  views.talentos_edit2,   name='talentos_edit2'),

    url(r'^talentos_lista/(?P<cadastro>\d+)/$', views.talentos_lista, name='talentos_lista'), 
    url(r'^talentos_detalhe/(?P<pk>\d+)/$', views.talentos_detalhe, name='talentos_detalhe'),


    url(r'^dica1$', views.dica1, name='dica1'),
    url(r'^funcionamento/$', views.funcionamento, name='funcionamento'), 
    url(r'^fundamentos/$', views.fundamentos, name='fundamentos'), 
    url(r'^saiba_mais/$', views.saiba_mais, name='saiba_mais'), 
    url(r'^seguranca/$', views.seguranca, name='seguranca'), 

    url(r'^lista/$', views.cadastro_list, name='cadastro_list'),    
    url(r'^movimentacao/(?P<pk>\d+)/$', views.movimentacao, name='movimentacao'),

    url(r'^talento_list/$', views.talento_list, name='talento_list'),
    url(r'^talento/add/$',	views.talento_crud,	name='talento_crud'),
    url(r'^talento/(?P<pk>\d+)/$',	views.talento_detail,	name='talento_detail'),
    url(r'^talento/(?P<pk>\d+)/edit',  views.talento_edit,   name='talento_edit'),
    url(r'^talento/(?P<pk>\d+)/del',  views.talento_del,   name='talento_del'),
    

    url(r'^geral/$', views.cadastro_list, name='geral'), 
    
    url(r'^cadastro/new/$',	views.assoc_crud,	name='assoc_crud'),
    url(r'^cadastro/(?P<pk>\d+)/$',	views.assoc_crud,	name='cadastro_detail'),
    url(r'^assoc/add/$',  views.assoc_add, name='assoc_add'),     

    url(r'^lancamento/(?P<pk>\d+)/$', views.lancamento_detail, name='lancamento_detail'),
    url(r'^lancamento/new/$',	views.lancamento_new,	name='lancamento_new'),
 
    url(r'^nome-autocomplete/$',    NomeAutocomplete.as_view(), name='nome-autocomplete',),
    
]




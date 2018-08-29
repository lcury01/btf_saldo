
from django.conf.urls import url
from . import views


from btf_saldo.views import NomeAutocomplete


urlpatterns = [
#home    
    url(r'^$', views.home, name='home'),
    url(r'^index_saiba', views.index_saiba, name='index_saiba'),
    url(r'^index_funciona', views.index_funciona, name='index_funciona'),
    url(r'^index_grupo', views.index_grupo, name='index_grupo'),
    url(r'^index_ajudar', views.index_ajudar, name='index_ajudar'),
    url(r'^index_porque', views.index_porque, name='index_porque'),
    url(r'^index_eventos', views.index_eventos, name='index_eventos'),
    url(r'^index_definir', views.index_definir, name='index_definir'),


#operacao
    url(r'^operacao', views.operacao,name='operacao'),    
    url(r'^libera_lista', views.libera_lista, name='libera_lista'),
    url(r'^desbloquear/(?P<pk>\d+)/$', views.desbloquear, name='desbloquear'), 
    url(r'^assoc/add/$',  views.assoc_add, name='assoc_add'), 
    url(r'^cadastro/(?P<pk>\d+)/$', views.assoc_crud,   name='cadastro_detail'),
    url(r'^bloquear/(?P<pk>\d+)/$', views.bloquear, name='bloquear'), 
    url(r'^talentos_filtro', views.talentos_filtro, name='talentos_filtro'), 
    url(r'^talentos/(?P<pk>\d+)/edit2',  views.talentos_edit2,   name='talentos_edit2'),
    url(r'^talentos_lista/(?P<cadastro>\d+)/$', views.talentos_lista, name='talentos_lista'), 
    url(r'^talentos_detalhe/(?P<pk>\d+)/$', views.talentos_detalhe, name='talentos_detalhe'),

    url(r'^associados', views.assoc_home, name='assoc_home'),
    url(r'^transferencia', views.transferencia,name='transferencia'),
    url(r'^administrativo', views.administrativo,name='administrativo'),
    url(r'^eventos', views.eventos,name='eventos'),


#associados
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
    
    url(r'^precadastro$',  views.precadastro, name='precadastro'),
    url(r'^precadastro/new/$',	views.precadastro_crud,	name='precadastro_crud'),

        

    url(r'^lancamento/(?P<pk>\d+)/$', views.lancamento_detail, name='lancamento_detail'),
    url(r'^lancamento/new/$',	views.lancamento_new,	name='lancamento_new'),
 
    url(r'^nome-autocomplete/$',    NomeAutocomplete.as_view(), name='nome-autocomplete',),
    
]




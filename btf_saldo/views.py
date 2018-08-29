from datetime import date
from django.utils import timezone
from django.shortcuts import render, get_object_or_404, redirect


from dal import autocomplete

from .filters import TalentosFilter

from .models import Cadastro
from .models import CadastroAUX
from .models import PreCadastro
from .models import Lancamento
from .models import Transferencia
from .models import Talento

from .forms import LancamentoForm
from .forms import TalentoForm
from .forms import CadastroForm
from .forms import PreCadastroForm
from .forms import AssocForm

# a partir daqui

def home(request):
	return 	render(request, 'btf_saldo/index.html')

def index_funciona(request):
    return  render(request, 'btf_saldo/index_funciona.html')

def index_porque(request):
    return  render(request, 'btf_saldo/index_porque.html')    

def index_grupo(request):
    return  render(request, 'btf_saldo/index_grupo.html')

def index_ajudar(request):
    return  render(request, 'btf_saldo/index_ajudar.html')

def index_saiba(request):
    return  render(request, 'btf_saldo/index_saiba.html')

def index_eventos(request):
    return  render(request, 'btf_saldo/index_eventos.html')

def index_definir(request):
    return  render(request, 'btf_saldo/index_definir.html')




def assoc_home(request):
    return  render(request, 'btf_saldo/inicio.html')


def operacao(request):
    return  render(request, 'btf_saldo/inicio_operacao.html', {'operacao': True})

def transferencia(request):
    return  render(request, 'btf_saldo/inicio_operacao.html', {'operacao': True})

def eventos(request):
    return  render(request, 'btf_saldo/inicio_operacao.html', {'operacao': True})

def administrativo(request):
    return  render(request, 'btf_saldo/inicio_operacao.html', {'operacao': True})

def libera_lista(request):
    data=date.today()
    data30=date.fromordinal(data.toordinal()-30)

    bloqs = Cadastro.objects.filter(dt_cadastro__date__lt=data30)
    return  render(request, 'btf_saldo/libera_lista.html', {'bloqs':bloqs, 'data':data, 'data30':data30, 'operacao': True})

def desbloquear(request, pk):
    
    if request.method == "POST":
        bloqs = get_object_or_404(Cadastro, pk=pk)
        bloqs.libera()

        data=date.today()
        data30=date.fromordinal(data.toordinal()-30)

        bloqs = Cadastro.objects.filter(dt_cadastro__date__lt=data30)
        return  render(request, 'btf_saldo/libera_lista.html', {'bloqs':bloqs, 'data':data, 'data30':data30, 'operacao': True})
    
    else:       
        bloqs2 = get_object_or_404(Cadastro, pk=pk)
        return render(request, 'btf_saldo/libera_detalhe.html', {'bloqs2': bloqs2, 'operacao': True})

def bloquear(request, pk):
    
    if request.method == "POST":
        bloqs = get_object_or_404(Cadastro, pk=pk)
        bloqs.bloqueia()

        data=date.today()
        data30=date.fromordinal(data.toordinal()-30)

        bloqs = Cadastro.objects.filter(dt_cadastro__date__lt=data30)
        return  render(request, 'btf_saldo/libera_lista.html', {'bloqs':bloqs, 'data':data, 'data30':data30, 'operacao': True})
    
    else:       
        bloqs2 = get_object_or_404(Cadastro, pk=pk)
        return render(request, 'btf_saldo/libera_detalhe.html', {'bloqs2': bloqs2, 'operacao': True})

def cadastro_list(request):    
    cadastros   =   Cadastro.objects.all()
    return  render(request, 'btf_saldo/assoc_list.html',  {'cadastros':cadastros, 'operacao': True})      

def cadastro_detail(request, pk):
    cadastros = get_object_or_404(Cadastro, pk=pk)
    return render(request, 'btf_saldo/assoc_detail.html', {'cadastros': cadastros, 'operacao': True})


def assoc_crud(request, pk):
    cadastros = get_object_or_404(Cadastro, pk=pk)
    if request.method == "POST":
        form = AssocForm(request.POST,instance=cadastros)
        if form.is_valid():
            cadastros = form.save(commit=False)
            cadastros.save()
            #return redirect('btf_saldo.views.cadastro_list')   
            return  redirect('cadastro_list')    
    else:       
        form    =   AssocForm(instance=cadastros)
    return  render(request, 'btf_saldo/assoc_edit.html', {'form':    form, 'operacao': True})    

def assoc_add(request):
    if request.method == "POST":

        form = AssocForm(request.POST)
        if form.is_valid():
            cadastros = form.save(commit=False)
            cadastros.saldo_inicial= 4;
            cadastros.liberado = False;
            cadastros.save()
        
            return  redirect('cadastro_list')    
    else:       
        form    =   AssocForm()
        return  render(request, 'btf_saldo/assoc_edit.html', {'form':    form, 'operacao': True})
   

def talentos_filtro(request):
    talentos_list = Talento.objects.all()
    talentos_filter = TalentosFilter(request.GET, queryset=talentos_list)
    return render(request, 'btf_saldo/talentos_filtro.html', {'filter': talentos_filter, 'operacao': True})
    #return render(request, 'btf_saldo/talentos_filtro_new.html')

def talentos_edit2(request, pk):
    talento = get_object_or_404(Talento, pk=pk)
    if request.method == "POST":
        form = TalentoForm(request.POST, instance=talento)
        if form.is_valid():
            talento = form.save(commit=False)
            talento.save()
            return redirect('talentos_filtro')   
    else:
        form = TalentoForm(instance=talento)
    return render(request, 'btf_saldo/talento_edit.html', {'form': form, 'operacao': True})    


def talento_del(request, pk):
    talento = get_object_or_404(Talento, pk=pk)
    if request.method == "POST":
            talento.delete()
            return redirect('talentos_filtro')   
    else:
        form = TalentoForm(instance=talento)
    return render(request, 'btf_saldo/talento_del.html', {'form': form, 'operacao': True})    


def talentos_lista(request, cad):
    return  render(request, 'btf_saldo/funcionamento.html')

def talentos_detalhe(request, pk):
    return  render(request, 'btf_saldo/funcionamento.html')



def funcionamento(request):
    return  render(request, 'btf_saldo/funcionamento.html')

def fundamentos(request):
    return  render(request, 'btf_saldo/fundamentos.html')

def saiba_mais(request):
    return  render(request, 'btf_saldo/saiba_mais.html')

def seguranca(request):
    return  render(request, 'btf_saldo/seguranca.html')

def dica1(request):
	return 	render(request, 'btf_saldo/dica1.html')

def geral(request):    
    cadastros   =   Cadastro.objects.all()
    return  render(request, 'btf_saldo/geral.html',  {'cadastros':cadastros})    

def precadastro(request):       
    return  render(request, 'btf_saldo/precadastro.html')    

def precadastro_crud(request):
	if request.method == "POST":
		form = PreCadastroForm(request.POST)
		if form.is_valid():
			precadastro = form.save(commit=False)
			precadastro.save()
			#return	redirect('btf_saldo.views.cadastro_list')	
			return	render(request,	'btf_saldo/cadastro_edit.html',	{'form':	form})    
	else:		
		form	=	PreCadastroForm()
	return	render(request,	'btf_saldo/cadastro_edit.html',	{'form':	form})    

def movimentacao(request, pk):    
    transfs = Transferencia.objects.filter(quem=pk).order_by('data')
    return render(request, 'btf_saldo/movimentacao.html',  {'transfs':transfs})

def lancamento_detail(request, pk):
    lancamento = get_object_or_404(Lancamento, pk=pk)
    return render(request, 'btf_saldo/lancamento_detail.html', {'lancamento': lancamento})

def lancamento_new(request):
	if request.method == "POST":
		form = LancamentoForm(request.POST)
		if form.is_valid():
			lancamento = form.save(commit=False)
			lancamento.save()
			return	redirect('lancamento_detail',	pk=lancamento.pk)	
	else:		
		form	=	LancamentoForm()
	return	render(request,	'btf_saldo/lancamento_edit.html',	{'form':	form})    

def talento_list(request):    
    talentos   =   Talento.objects.filter(quem__liberado=True).order_by('talentoclasse','regiao')
    return  render(request, 'btf_saldo/talento_list.html',  {'talentos':talentos})    

def talento_crud(request):
    
    if request.method == "POST":
        form = TalentoForm(request.POST)
        if form.is_valid():
            talento = form.save(commit=False)
            talento.save()
            return redirect('talento_edit', pk=talento.pk)
    else:
        form = TalentoForm()
    return render(request, 'btf_saldo/talento_crud.html', {'form': form})    


def talento_detail(request, pk):
    talento = get_object_or_404(Talento, pk=pk)
    return render(request, 'btf_saldo/talento_detail.html', {'talento': talento})

def talento_edit(request, pk):
    talento = get_object_or_404(Talento, pk=pk)
    if request.method == "POST":
        form = TalentoForm(request.POST, instance=talento)
        if form.is_valid():
            talento = form.save(commit=False)
            talento.save()
            return redirect('talento_detail', pk=talento.pk)
    else:
        form = TalentoForm(instance=talento)
    return render(request, 'btf_saldo/talento_edit.html', {'form': form})    


class NomeAutocomplete(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        # Don't forget to filter out results depending on the visitor !
        #if not self.request.user.is_authenticated():
        #    return Cadastro.objects.none()

        qs = Cadastro.objects.filter(liberado=True)

        if self.q:
            qs = qs.filter(nome__istartswith=self.q)

        return qs



from django.utils import timezone
from django.shortcuts import render, get_object_or_404, redirect


from .models import Cadastro
from .models import CadastroAUX
from .models import Lancamento2
from .models import Transferencia
from .models import Talento
from .forms import LancamentoForm
from .forms import TalentoForm
from .forms import CadastroForm


# a partir daqui

def home(request):
	return 	render(request, 'btf_saldo/home.html')

def geral(request):    
    cadastros   =   Cadastro.objects.all()
    return  render(request, 'btf_saldo/geral.html',  {'cadastros':cadastros})    

def cadastro_list(request):    
    cadastros   =   Cadastro.objects.all()
    return  render(request, 'btf_saldo/cadastro_list.html',  {'cadastros':cadastros})    

def cadastro_detail(request, pk):
    cadastros = get_object_or_404(Cadastro, pk=pk)
    return render(request, 'btf_saldo/cadastro_detail.html', {'cadastros': cadastros})

def cadastro_crud(request):
	if request.method == "POST":
		form = CadastroForm(request.POST)
		if form.is_valid():
			cadastro = form.save(commit=False)
			cadastro.save()
			#return	redirect('btf_saldo.views.cadastro_list')	
			return	render(request,	'btf_saldo/cadastro_edit.html',	{'form':	form})    
	else:		
		form	=	CadastroForm()
	return	render(request,	'btf_saldo/cadastro_edit.html',	{'form':	form})    

def movimentacao(request, pk):    
    transfs = Transferencia.objects.filter(quem=pk).order_by('data')
    return render(request, 'btf_saldo/movimentacao.html',  {'transfs':transfs})

def lancamento_detail(request, pk):
    lancamento = get_object_or_404(Lancamento2, pk=pk)
    return render(request, 'btf_saldo/lancamento_detail.html', {'lancamento': lancamento})

def lancamento_new(request):
	if request.method == "POST":
		form = LancamentoForm(request.POST)
		if form.is_valid():
			lancamento = form.save(commit=False)
			lancamento.save()
			return	redirect('btf_saldo.views.lancamento_detail',	pk=lancamento.pk)	
	else:		
		form	=	LancamentoForm()
	return	render(request,	'btf_saldo/lancamento_edit.html',	{'form':	form})    

def talento_list(request):    
    talentos   =   Talento.objects.all()
    return  render(request, 'btf_saldo/talento_list.html',  {'talentos':talentos})    

def talento_crud(request):    
	if request.method == "POST":
		form = TalentoForm(request.POST)
		if form.is_valid():
			talento = form.save(commit=False)
			talento.save()
			return	redirect('btf_saldo.views.talento_detail',	pk=talento.pk)	
	else:		
		form	=	TalentoForm()
	return	render(request,	'btf_saldo/talento_crud.html',	{'form':	form})    

def talento_detail(request, pk):
    talento = get_object_or_404(Talento, pk=pk)
    return render(request, 'btf_saldo/talento_detail.html', {'talento': talento})

from dal import autocomplete

from django import forms

from .models import Lancamento2
from .models import Cadastro
from .models import CadastroAUX
from .models import Regiao
from .models import TalentoClasse
from .models import Talento

class	LancamentoForm(forms.ModelForm):
	class	Meta:
		model	=	Lancamento2
		fields	=	('debito_fk','credito_fk','descricao','valor')
		#fields	=	('credito_fk','credito_nm',	'debito_nm', 'valor',)
		

class	CadastroForm(forms.ModelForm):
	class	Meta:
		model	=	Cadastro
		fields	=	('nome','conta','saldo_inicial')


class TalentoForm(forms.ModelForm):	
   class 	Meta:
    	model 	= 	Talento
    	fields 	= 	('quem','regiao','experiencia')
    	widgets = 	{
				'quem': autocomplete.ModelSelect2(url='quem-autocomplete')
		}
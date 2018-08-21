from dal import autocomplete

from django import forms

from .models import Lancamento
from .models import Cadastro
from .models import CadastroAUX
from .models import PreCadastro
from .models import Regiao
from .models import TalentoClasse
from .models import Talento

#from .filters import TalentosFiltro

class	LancamentoForm(forms.ModelForm):
	class	Meta:
		model	=	Lancamento
		fields	=	('debito_fk','credito_fk','descricao','valor')
		widgets = 	{
				'debito_fk': autocomplete.ModelSelect2(url='nome-autocomplete'),
				'credito_fk': autocomplete.ModelSelect2(url='nome-autocomplete')
		}
		#fields	=	('credito_fk','credito_nm',	'debito_nm', 'valor',)
		

class	CadastroForm(forms.ModelForm):
	class	Meta:
		model	=	Cadastro
		fields	=	('nome','conta','saldo_inicial')

class	AssocForm(forms.ModelForm):
	class	Meta:
		model	=	Cadastro
		fields	=	('nome','dt_cadastro')

class	PreCadastroForm(forms.ModelForm):
	class	Meta:
		model	=	PreCadastro
		fields	=	( 'nome', 'nomefb', 'paginafb', 'localizacao', 'celular', 'celular_visivel', 'email', 'senha', 'cadastro_fk', 
						'nm_referencia1', 'tel_referencia1', 'fb_referencia1', 'nm_referencia2', 'tel_referencia2', 'fb_referencia2', 'nm_referencia3', 'tel_referencia3', 'fb_referencia3', 'comosoube', 'sabecomoparticipar') 

class	PreCadastro_1Form(forms.ModelForm):
	class	Meta:
		model	=	PreCadastro
		fields	=	( 'nome', 'nomefb', 'paginafb','cadastro_fk','comosoube', 'sabecomoparticipar')
class	PreCadastro_2Form(forms.ModelForm):
	class	Meta:
		model	=	PreCadastro
		fields	=	( 'localizacao', 'celular', 'celular_visivel') 

class	PreCadastro_3Form(forms.ModelForm):
	class	Meta:
		model	=	PreCadastro
		fields	=	( 'email', 'senha', 'cadastro_fk')

class	PreCadastro_4Form(forms.ModelForm):
	class	Meta:
		model	=	PreCadastro
		fields	=	('nm_referencia1', 'tel_referencia1', 'fb_referencia1', 'nm_referencia2', 'tel_referencia2', 'fb_referencia2', 'nm_referencia3', 'tel_referencia3', 'fb_referencia3')

class ModelChoiceField2(forms.ModelMultipleChoiceField):
    def label_from_instance(self, obj):
        return "My Object #%i" % obj.name

class TalentoForm(forms.ModelForm):	
   class 	Meta:
    	model 	= 	Talento
    	fields 	= 	('quem', 'regiao', 'talentoclasse', 'descricao', 'experiencia')
    	widgets = 	{
				'quem': autocomplete.ModelSelect2(url='nome-autocomplete')
		}

    	
    	




		
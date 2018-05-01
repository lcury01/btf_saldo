from django.db import models
from django.utils import timezone

class Cadastro(models.Model):
    				nome 	= 	models.CharField("Nome do Associado", max_length=50)
    				conta 	=	models.CharField("Conta BTF", max_length=7)
    				saldo_inicial 	= 	models.DecimalField("Saldo Inicial em Creditos de Tempo", max_digits=4,decimal_places=1)
    				def	__str__(self):
									return	self.nome

class CadastroAUX(models.Model):
                    nome    =   models.CharField("Nome do Associado", max_length=50)
                    conta   =   models.CharField("Conta BTF", max_length=7)
                    def __str__(self):
                                    return  self.nome

class Lancamento2(models.Model):                        
                    debito_fk   =   models.ForeignKey(Cadastro, verbose_name = "area do talento")
                    credito_fk  =   models.ForeignKey(CadastroAUX, verbose_name="quem recebe os créditos")
                    descricao   =   models.CharField("Qual foi a troca", max_length=100)
                    valor       =   models.DecimalField("Créditos de Tempo", max_digits=4,decimal_places=2)
                    dttroca     =   models.DateField("quando foi a troca",default=timezone.now)
                    dtinclusao  =   models.DateTimeField("inclusao registro",default=timezone.now)
                    def __str__(self):
                                    return  self.descricao

class Transferencia (models.Model):
    quem=models.ForeignKey(Cadastro)
    descricao = models.CharField("Qual foi a troca", max_length=100)
    comquem = models.CharField("Com que trocou", max_length=50, default='')
    valor = models.DecimalField("Créditos de Tempo", max_digits=4,decimal_places=2)
    data = models.DateTimeField("Data da Transferência", default=timezone.now)
    sinal = models.CharField("Sinal", max_length=1)

class TalentoClasse (models.Model):
    descricao = models.CharField("Qual a área do Talento", max_length=100)
    def __str__(self):
                    return  self.descricao

class Regiao (models.Model):
    descricao = models.CharField("Regiao", max_length=100)
    def __str__(self):
                    return  self.descricao

class Talento (models.Model):
    talentoclasse = models.ForeignKey(TalentoClasse, verbose_name = "area do talento")
    quem = models.ForeignKey(Cadastro, verbose_name = "Associado")
    descricao = models.CharField("descreva seu talento", max_length=100)
    experiencia = models.CharField("sua experiência", max_length=100)
    regiao = models.ForeignKey(Regiao, verbose_name = "Regiao")
    def __str__(self):
                    return  self.descricao

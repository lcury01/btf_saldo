from django.db import models
from django.utils import timezone
from dal import autocomplete


class Cadastro(models.Model):
    				nome            =   models.CharField("Nome do Associado", max_length=50)
    				conta 	        =	models.CharField("Conta BTF", max_length=7)
    				saldo_inicial	=	models.DecimalField("Saldo Inicial em Creditos de Tempo", max_digits=4,decimal_places=1)
    				dt_cadastro	=	models.DateTimeField(default=timezone.now)
    				dt_bloqueio	=	models.DateTimeField(blank=True, null=True)
    				dt_liberado	=	models.DateTimeField(blank=True, null=True)
    				liberado 	=	models.BooleanField(default=False)
    				
    				def	__str__(self):
									return	self.nome

    				def	bloqueia(self):
    						self.dt_bloqueio	=	timezone.now()
    						self.liberado 		=	False
    						self.save()
    						return	self.dt_bloqueio

    				def	libera(self):
    						self.dt_liberado	=	timezone.now()
    						self.liberado 		=	True
    						self.save()
    						return	self.dt_liberado


class PreCadastro(models.Model):
                    nome    =   models.CharField("qual o seu nome?",max_length=50)
                    nomefb  =   models.CharField("qual o nome que você usa no facebook?", max_length=50)
                    paginafb    =   models.CharField("cole aqui a URL ou link do seu perfil no facebook",max_length=150)
                    localizacao =   models.CharField("onde você mora",max_length=100)
                    celular    =   models.CharField("seu telefone",max_length=11)
                    celular_visivel  =   models.BooleanField("Permite divulgar o seu telefone para outros associados?")
                    email   =   models.CharField("informe seu email",max_length=50)
                    senha   =   models.CharField("informe uma senha",max_length=10)
                    cadastro_fk =   models.ForeignKey(Cadastro,on_delete=models.CASCADE,verbose_name="Quem é vc no nosso cadastro")
                    emailconfirmado = models.BooleanField("email confirmado")
                    nm_referencia1 =   models.CharField("Referência Pessoal 1",max_length=50)
                    tel_referencia1 =   models.CharField("Telefone Referência 1",max_length=11)
                    fb_referencia1  =   models.CharField("Perfil Facebook Referencia1",max_length=150)
                    nm_referencia2 =   models.CharField("Referência Pessoal 2",max_length=50)
                    tel_referencia2 =   models.CharField("Telefone Referência 2",max_length=11)
                    fb_referencia2  =   models.CharField("Perfil Facebook Referencia2",max_length=150)
                    nm_referencia3 =   models.CharField("Referência Pessoal 3",max_length=50)
                    tel_referencia3 =   models.CharField("Telefone Referência 3",max_length=11)
                    fb_referencia3  =   models.CharField("Perfil Facebook Referencia3",max_length=150)
                    comosoube   =   models.TextField("como soube do Banco de Tempo",max_length=300)
                    sabecomoparticipar  =   models.TextField("já sabe como participar do grupo",max_length=500)

    

class CadastroAUX(models.Model):
                    nome    =   models.CharField("Nome do Associado", max_length=50)
                    conta   =   models.CharField("Conta BTF", max_length=7)
                    def __str__(self):
                                    return  self.nome

class Lancamento(models.Model):                        
                    debito_fk   =   models.ForeignKey(Cadastro, on_delete=models.CASCADE, verbose_name = "quem transfere os creditos")
                    credito_fk  =   models.ForeignKey(CadastroAUX, verbose_name="quem recebe os créditos", on_delete=models.CASCADE)
                    descricao   =   models.CharField("Qual foi a troca", max_length=100)
                    valor       =   models.DecimalField("Créditos de Tempo", max_digits=4,decimal_places=2)
                    dttroca     =   models.DateField("quando foi a troca",default=timezone.now)
                    dtinclusao  =   models.DateTimeField("inclusao registro",default=timezone.now)
                    dtprocesso  =   models.DateTimeField("processo")
                    status      =   models.CharField("Status", max_length=2, help_text="Status do Lacamento")
                    def __str__(self):
                                    return  self.descricao

class Transferencia (models.Model):
    quem=models.ForeignKey(Cadastro, on_delete=models.CASCADE)
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
    talentoclasse = models.ForeignKey(TalentoClasse, verbose_name = "area do talento", on_delete=models.CASCADE)
    descricao = models.TextField("seu Talento", max_length=1000,help_text="Descreva como vc quer oferecer seu talento ao grupo BTF")
    experiencia = models.TextField("experiência", max_length=1000,help_text="Nos conte qual a sua experiência com esse talento. Isso fica apenas nos nossos registros, para ações maiores do BTF, quando precisarmos de talentos bem especificos nos eventos em grupo ou projetos sociais")
    regiao = models.ForeignKey(Regiao, verbose_name = "Região de Atuação", help_text="Regiao onde vc pode ajudar com seu talento", on_delete=models.CASCADE)
    quem = models.ForeignKey(Cadastro, verbose_name="quem é você", help_text="Digite seu nome igual a planilha de Créditos", on_delete=models.CASCADE )
    def __str__(self):
                    return  self.descricao
    def cadquem(self):
                    return  self.quem



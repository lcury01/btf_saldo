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
                    debito_fk   =   models.ForeignKey(Cadastro, verbose_name = "qum transfere os creditos")
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
    quem = models.ForeignKey(Cadastro, verbose_name = "Associado",help_text="Quem é você no BTF? Seu nome igual ao da planilha de créditos")
    descricao = models.TextField("seu Talento", max_length=1000,help_text="Descreva como vc quer oferecer seu talento ao grupo BTF")
    experiencia = models.TextField("experiência", max_length=1000,help_text="Nos conte qual a sua experiência com esse talento. Isso fica apenas nos nossos registros, para ações maiores do BTF, quando precisarmos de talentos bem especificos nos eventos em grupo ou projetos sociais")
    regiao = models.ForeignKey(Regiao, verbose_name = "Região de Atuação",help_text="Regiao onde vc pode ajudar com seu talento")
    def __str__(self):
                    return  self.descricao



class Reputacao (models.Model)
    quemavalia  =   models.ForeignKey(Cadastro,verbose_name = 'quem é você')
    avaliado    =   models.ForeignKey(CadastroAUX,verbose_name  =   'quem vc quer avaliar ?')
    tpavaliacao =   models.
Vc quer avaliar 
    o associado oferecendo o talento a você
    o associado recebendo o talento que vc ofereceu

Qual o tipo da troca ?
Atividade em Grupo pontual - evento, aula única, palestra, oficina, etc.
Atividade em Grupo de longo tempo - cursos, aulas, terapias com mais de uma sessão, etcc.
Troca simples enveolvendo produto ou serviço

Qual foi a troca ?

Como você e o associado se encontraram ?


Publiquei meu talento ou minha necessidadeno grupo de trocas
Respondendo a uma postagem no grupo de trocas.
Pelos comentários em postagens de outras pessoas no grupo
Através da planilha de talentos (procurei/am pelo taleto )
Fui recomendado por outro associado fora do grupo do BTF
A gente mantém contato fora do BTF e negociamos as trocas fora do BTF
É uma atividade de longo tempo
Outro


Qual a sua avaliação ?
💛Super Recomendo! Sem atrasos, sem faltas, boa comunicação
🙂Recomendo! Se houve falha, desencontro ou falta, foi justificada
👍 Foi uma negociação normal
🤝 Foi uma negociação um pouquinho dificil, mas tudo se resolveu da melhor forma.
👎Tive problemas (Não compareceu, não cumpriu com o combinado, não se comunicou bem comigo)


Deixe aqui um comentário publico sobre a troca... se o campo for preenchido, a outra pessoa terá acesso ao seu nome na avaliação.

Se houve problemas, é importante que vc nos explique melhor para mantermos as boas relações no grupo
Associado não seguiu as regras na negociação (por exemplo, cobrou pelo serviço ou está pedindo horas a mais pelo talento)
Encontrei o associado na planilha de talentos, mas ele não responde 
Estou tentando contato por motivos diversos com associado e ele não me responde
Associado não transferiu os creditos adequadamente.
Outros problemas


Quer nos contar alguma coisa sobre troca? Só os administradores tem acesso a este campo


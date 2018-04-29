#!/usr/bin/env python


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.9/howto/static-files/




#if __name__ == "__main__":


#from models import Cadastro

#from models import Transferencia

# abrir lançamentos que não estão processados
# verificar se pessoa tem saldo
# transferir o saldo, sempre
# gerar arquivo .cvs para publicação dos creditos

####--------------------- validações
##     atuais	
#  se quem transfere tem saldo

##     validações não implementadas
#  uma das pessoas não está mais ativa
#  se quem está recebendo o credito pode receber o credito (fluxo novo de cadastro)
#  duplicidade de cadastro

#class Lancamento2(models.Model):                        
#                    debito_fk   =   models.ForeignKey(Cadastro, verbose_name="quem transfere os créditos")
#                    credito_fk  =   models.ForeignKey(CadastroAUX, verbose_name="quem recebe os créditos")
#                    descricao   =   models.CharField("Qual foi a troca", max_length=100)
#                    valor       =   models.DecimalField("Créditos de Tempo", max_digits=4,decimal_places=2)
#                    dttroca     =   models.DateField("quando foi a troca",default=timezone.now)
#                    dtinclusao  =   models.DateTimeField("inclusao registro",default=timezone.now)
#                    def __str__(self):
#                                    return  self.descricao

#Transfs = Lancamento.objects.all()

#for transf in Transfs:
	#Quem_transfere = get_object(Cadastro,Transf.debito_fk,pk)
#	print (Transfs)


import sqlite3
# Cria uma conexão e um cursor
con = sqlite3.connect('emails.db')
cur = con.cursor()
# Cria uma tabela
sql = 'create table emails '\
'(id integer primary key, '\
'nome varchar(100), '\
'email varchar(100))'
cur.execute(sql)
# sentença SQL para inserir registros
sql = 'insert into emails values (null, ?, ?)'
# Dados
recset = [('jane doe', 'jane@nowhere.org'),
('rock', 'rock@hardplace.com')]
# Insere os registros
for rec in recset:
cur.execute(sql, rec)
# Confirma a transação
con.commit()
# Seleciona todos os registros
cur.execute('select * from emails')
# Recupera os resultados
recset = cur.fetchall()
# Mostra
for rec in recset:
print '%d: %s(%s)' % recBanco de dados
169
# Fecha a conexão
con.close()
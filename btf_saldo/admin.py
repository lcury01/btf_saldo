from django.contrib import admin

from .models import Cadastro
from .models import CadastroAUX
from .models import Lancamento2
from .models import Transferencia
from .models import Regiao
from .models import TalentoClasse
from .models import Talento


admin.site.register(Cadastro)
admin.site.register(CadastroAUX)
admin.site.register(Lancamento2)
admin.site.register(Transferencia)
admin.site.register(TalentoClasse)
admin.site.register(Talento)
admin.site.register(Regiao)



# Register your models here.

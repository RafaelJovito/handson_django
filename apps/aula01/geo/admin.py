from django.contrib.admin import ModelAdmin, register
from .models import UF, Municipio, Edital


@register(UF)
class UFAdmin(ModelAdmin):
    list_display = ('sigla', 'nome', 'codigo')


@register(Municipio)
class MunicipioAdmin(ModelAdmin):
    list_display = ('codigo', 'uf', 'nome')
    list_editable = ('uf', 'nome')
    list_filter = ('uf__nome', )
    search_fields = ('nome', 'codigo')


@register(Edital)
class EditalAdmin(ModelAdmin):
    list_display = ('tipo', 'programa', 'numero', 'sigla', 'linkEdital', 'descricao')
    list_editable = ('programa', 'numero', 'sigla', 'descricao')
    list_filter = ('tipo', 'programa', 'numero', 'sigla')
    search_fields = ('tipo', 'programa', 'numero', 'sigla')

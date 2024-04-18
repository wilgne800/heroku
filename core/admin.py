from django.contrib import admin

from .models import Poduto, Cliente

class ProdutoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'descricao', 'estoque')

class ClienteAdmin(admin.ModelAdmin):
    list_display = ('nome', 'sobrenome', 'emal')

admin.site.register(Poduto, ProdutoAdmin)
admin.site.register(Cliente, ClienteAdmin)
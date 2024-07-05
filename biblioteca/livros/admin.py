from django.contrib import admin
from .models import Livro

class ExibeLivro(admin.ModelAdmin):
    list_display = ('id','titulo','autor', 'ano_publicacao', 'isbn', 'emprestado')
    list_display_links = ('id','titulo')
    search_fields = ('titulo',)
    list_filter = ('ano_publicacao',)
    list_editable = ('emprestado',)
    list_per_page = 5


admin.site.register(Livro, ExibeLivro)
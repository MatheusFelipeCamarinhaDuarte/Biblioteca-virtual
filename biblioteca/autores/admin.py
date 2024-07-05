from django.contrib import admin
from .models import Autor

class ExibeAutor(admin.ModelAdmin):
    list_display = ('id','nome')
    list_display_links = ('id','nome')
    search_fields = ('nome',)
    list_filter = ('nacionalidade',)
    list_per_page = 5


admin.site.register(Autor,ExibeAutor)
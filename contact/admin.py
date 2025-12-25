from django.contrib import admin
from contact import models
# Register your models here.
#podemos ter essa class como configura~]ao do models no Admin do Django
@admin.register(models.Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = 'id', 'first_name', 'last_name', 'phone',
    ordering = 'id', #ordena pela coluna id
    search_fields = 'id', 'first_name', 'last_name', #pesquisar por categorias x no caso dterinada
    list_per_page = 10 #numero de itens por pagina
    list_max_show_all = 200 #maximo de itens que podem ser mostrados na pagina
    
    
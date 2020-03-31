from django.contrib import admin

# Register your models here.
from core.models import Trip, Classification

class displayViagensAdmin(admin.ModelAdmin):
    list_display = ('id', 'user_id', 'classificacao', 'nota')
    list_display_links = ('id', 'user_id', 'classificacao')
    search_fields = ('classificacao__classificacao', 'nota')
    list_filter = ('classificacao__classificacao', 'user_id', 'nota')
    list_per_page = 15

class displayClassificacoesAdmin(admin.ModelAdmin):
    list_display = ('id', 'classificacao')
    list_display_links = ('id', 'classificacao')
    list_filter = ('classificacao',)

admin.site.register(Trip, displayViagensAdmin)
admin.site.register(Classification, displayClassificacoesAdmin)
# Registros/admin.py
from django.contrib import admin
from .models import Registro, Comentario
from django.contrib.admin.models import LogEntry


class ComentarioInline(admin.TabularInline):
    model = Comentario


class RegistroAdmin(admin.ModelAdmin):
    inlines = [ComentarioInline]


# LogEntry.objects.all().delete()

admin.site.register(Registro, RegistroAdmin)
admin.site.register(Comentario)


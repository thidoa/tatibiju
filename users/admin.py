from django.contrib import admin
from .models import Usuario

@admin.register(Usuario)
class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'tipo')
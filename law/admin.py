from django.contrib import admin
from .models import Services , SumData

@admin.register(SumData)
class SumDataAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone', 'subject', 'message', )

@admin.register(Services)
class ServicesAdmin(admin.ModelAdmin):
    list_display = ('image', 'title', 'prah', )
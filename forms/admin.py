from django.contrib import admin
from .models import F101



@admin.register(F101)
class F101Admin(admin.ModelAdmin):
    pass
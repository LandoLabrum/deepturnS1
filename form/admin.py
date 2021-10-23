from django.contrib import admin
from .models import one, one_question



@admin.register(one_question)
class one_questionsAdmin(admin.ModelAdmin):
    pass

@admin.register(one)
class oneAdmin(admin.ModelAdmin):
    pass
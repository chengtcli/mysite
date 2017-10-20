from django.contrib import admin

from .models import Question, Choice

class Choiceinline(admin.TabularInline):
    model = Choice
    extra = 3

class QuestionAdmin(admin.ModelAdmin):
    inlines = [Choiceinline]
admin.site.register(Question, QuestionAdmin)

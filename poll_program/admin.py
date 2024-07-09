from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Poll, Option, Select

class SelectBox(admin.TabularInline):
    model = Option
    extra = 4

class PollQnsAdmin(admin.ModelAdmin):
    list_display = ('poll_question', 'creating_time')
    inlines = [SelectBox]

class SelectAdmin(admin.ModelAdmin):
    list_display = ('user', 'option', 'selecting_time')
    list_filter = ('option', 'selecting_time')

admin.site.register(Poll, PollQnsAdmin)
admin.site.register(Option)
admin.site.register(Select, SelectAdmin)

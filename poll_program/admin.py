from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Poll, Option, Select

class SelectBox(admin.TabularInline):
    """
    Inline admin descriptor for Option model.
    Defines extra option fields to be displayed in the Poll admin view.

    Attributes:
        model (Option): The model to be displayed as an inline.
        extra (int): The number of extra forms to display.
    """
    model = Option
    extra = 4

class PollQnsAdmin(admin.ModelAdmin):
    """
    Admin view for Poll model.

    Attributes:
        list_display (tuple): Fields to be displayed in the admin list view.
        inlines (list): Inline models to be displayed in the admin detail view.
    """
    list_display = ('poll_question', 'creating_time')
    inlines = [SelectBox]

class SelectAdmin(admin.ModelAdmin):
    """
    Admin view for Select model.

    Attributes:
        list_display (tuple): Fields to be displayed in the admin list view.
        list_filter (tuple): Fields to filter the admin list view.
    """
    list_display = ('user', 'option', 'selecting_time')
    list_filter = ('option', 'selecting_time')

# Registering the models with the admin site
admin.site.register(Poll, PollQnsAdmin)
admin.site.register(Option)
admin.site.register(Select, SelectAdmin)

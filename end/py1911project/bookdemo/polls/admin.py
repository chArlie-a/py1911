from django.contrib import admin
from django.contrib.admin import ModelAdmin

from .models import *


# Register your models here.

class OptionInline(admin.StackedInline):
    """
    定义关联选项
    """
    model = Option
    extra = 1


class OptionAdmin(ModelAdmin):
    pass


class IssueAdmin(ModelAdmin):
    inlines = [OptionInline]


admin.site.register(Issue, IssueAdmin)
admin.site.register(Option, OptionAdmin)
admin.site.register(User)
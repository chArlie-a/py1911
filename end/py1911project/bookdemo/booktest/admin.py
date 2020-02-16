from django.contrib import admin
# 定义后端显示页面
from django.contrib.admin import ModelAdmin
# Register your models here.
#  django自带的后台管理操作需要在此实现
# 注册自己需要管理的模型 Book Hero
from .models import Book, Hero ,User,Account,Concact


class HeroInline(admin.StackedInline):
    """
    定义关联类
    """
    model = Hero
    extra = 1


class HeroAdmin(ModelAdmin):
    list_display = ("name", "gender", "content", "book")


class BookAdmin(ModelAdmin):
    list_display = ("title", "price", "pub_date")
    # 定义后端搜索字段
    search_fields = ("title",)
    # 指定过滤字段
    list_filter = ("title",)
    inlines = [HeroInline]


admin.site.register(Book, BookAdmin)
admin.site.register(Hero, HeroAdmin)
admin.site.register(User)
admin.site.register(Account)
admin.site.register(Concact)
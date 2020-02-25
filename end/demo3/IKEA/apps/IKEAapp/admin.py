from django.contrib import admin
from .models import *
# Register your models here.

admin.site.register(Ads)
admin.site.register(Category)
admin.site.register(Tag)
admin.site.register(Size)
admin.site.register(Color)
admin.site.register(Commodity)
admin.site.register(Comment)


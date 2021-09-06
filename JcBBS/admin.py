from django.contrib import admin
from JcBBS.models import *
# Register your models here.


class Province(admin.ModelAdmin):
    list_per_page = 10
    list_display = ('name', 'is_ftc', 'create_time', 'update_time')


class City(admin.ModelAdmin):
    list_per_page = 10
    list_display = ('name', 'province', 'is_ftc', 'create_time', 'update_time')


admin.site.register(Provinces, Province)
admin.site.register(Cities, City)
# admin.site.register(models.Block)
# admin.site.register(models.Articles_type)
# admin.site.register(models.Article_msg)
# admin.site.register(models.Articles)
# admin.site.register(models.Users)
# admin.site.register(models.Nymph_price)
# admin.site.register(models.Nymph_photo)

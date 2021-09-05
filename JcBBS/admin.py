from django.contrib import admin
from JcBBS import models
# Register your models here.


class Provinces(admin.ModelAdmin):
    list_per_page = 5
    list_display = ('name', 'create_time', 'update_time', 'is_ftc')


admin.site.register(models.Provinces)
admin.site.register(models.Cities)
admin.site.register(models.Block)
admin.site.register(models.Articles_type)
admin.site.register(models.Article_msg)
admin.site.register(models.Articles)
admin.site.register(models.Users)
admin.site.register(models.Nymph_price)
admin.site.register(models.Nymph_photo)

from django.contrib import admin
from JcBBS.models import *
# Register your models here.


class Province(admin.ModelAdmin):
    list_per_page = 30
    list_display = ('name', 'is_ftc', 'create_time', 'update_time')


class City(admin.ModelAdmin):
    list_per_page = 30
    list_display = ('name', 'province', 'is_ftc', 'create_time', 'update_time')


class Blocks(admin.ModelAdmin):
    list_per_page = 30
    list_display = ('name', 'city', 'create_time', 'update_time')


class User(admin.ModelAdmin):
    list_per_page = 30
    list_display = ('name', 'email', 'passwd', 'jc_coin',
                    'create_time', 'update_time')


class ArticlesType(admin.ModelAdmin):
    list_per_page = 30
    list_display = ('types', 'create_time', 'update_time')


class Article(admin.ModelAdmin):
    list_per_page = 30
    list_display = ('title', 'like', 'conllection', 'look',
                    'main_photo', 'buy_user_num', 'buy_num', 'user',
                    'block', 'article_type', 'create_time', 'update_time')


class ArticleMsg(admin.ModelAdmin):
    list_per_page = 30
    list_display = ('nymph_name', 'num', 'look_score', 'server_score',
                    'score', 'contact', 'address', 'main_body',
                    'article', 'create_time', 'update_time')


class Price(admin.ModelAdmin):
    list_per_page = 30
    list_display = ('types', 'price', 'article_msg', 'create_time', 'update_time')


class Photo(admin.ModelAdmin):
    list_per_page = 30
    list_display = ('pthoto_path', 'article_msg', 'create_time', 'update_time')


admin.site.register(Provinces, Province)
admin.site.register(Cities, City)
admin.site.register(Block, Blocks)
admin.site.register(Articles_type, ArticlesType)
admin.site.register(Article_msg, ArticleMsg)
admin.site.register(Articles, Article)
admin.site.register(Users, User)
admin.site.register(Nymph_price, Price)
admin.site.register(Nymph_photo, Photo)

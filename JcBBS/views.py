from django.shortcuts import render
from django.http import HttpResponse
from .models import Provinces, Cities, Block, Users,\
    Articles_type, Articles, Article_msg
from django.views.decorators.csrf import csrf_protect
from django.db import connection
import json


def index(request, pro_id=None, city_id=None, type_id=None):
    """主页"""
    if request.method == "GET":
        datas = {
            'types': dict(Articles_type.article_type),
            'pros': get_address_data(),
            'girls': get_index_data()
        }
        return render(request, "index.html", datas)
    if request.method == "POST":
        if pro_id is None:
            print(pro_id)
        else:
            raise print("pro_id为空")


def get_address_data():
    pros = Provinces.objects.all()
    tpros = {}
    for p in pros:
        citis = Cities.objects.filter(province_id=p.id)
        citis_list = []
        if p.is_ftc == 0:
            for c in citis:
                citis_list.append((c.id, c.name))
        else:
            blocks = Block.objects.filter(city=citis[0].id)
            for b in blocks:
                citis_list.append((b.id, b.name))
        tpros[p.id] = [p.name, citis_list]
    return tpros


def get_index_data():
    cursor = connection.cursor()
    sqlmsg = """
        select art.id, art.title, art.`like`, art.conllection, art.look, art.main_photo,
               art.buy_user_num, art.buy_num, art.create_time, art.user_id,
               jnp.types, jnp.price
        from jcbbs_articles as art
        left join jcbbs_article_msg as artm
            on art.id = artm.article_id
        left join jcbbs_nymph_price jnp
            on artm.id = jnp.article_msg_id
    """
    cursor.execute(sqlmsg)
    return cursor.fetchall()

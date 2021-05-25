from django.shortcuts import render
from django.http import HttpResponse
from .models import Provinces, Cities, Block, Users,\
    Articles_type, Articles, Article_msg
from django.views.decorators.csrf import csrf_protect
import json


def index(request, pro_id=None):
    """主页"""
    if request.method == "GET":
        ats = dict(Articles_type.article_type)
        pros = Provinces.objects.all()
        datas = {'types': ats, 'pros': {}}
        for p in pros:
            # print(p.id, p.name, p.is_ftc)
            citis = Cities.objects.filter(province_id=p.id)
            citis_list = []
            if p.is_ftc == 0:
                for c in citis:
                    # print(c.name)
                    citis_list.append((c.id, c.name))
            else:
                blocks = Block.objects.filter(city=citis[0].id)
                for b in blocks:
                    # print(b.name)
                    citis_list.append((b.id, b.name))
            datas['pros'][p.id] = [p.name, citis_list]
        return render(request, "index.html", datas)
    if request.method == "POST":
        if pro_id is None:
            print(pro_id)
        else:
            raise print("pro_id为空")



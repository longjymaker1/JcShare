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
        return render(request, "index.html", {'types': ats, 'pros': pros})
    if request.method == "POST":
        if pro_id is None:
            print(pro_id)
        else:
            raise print("pro_id为空")



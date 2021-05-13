from django.shortcuts import render
from django.http import HttpResponse
from .models import Provinces, Cities, Block, Users,\
    Articles_type, Articles,Article_msg
from django.views.decorators.csrf import csrf_protect
import json


def index(request):
    """主页"""
    if request.method == "GET":
        return render(request, "index.html")



from django.shortcuts import render
from django.http import HttpResponse
from .models import Provinces, Cities, Block, Users,\
    Articles_type, Articles, Article_msg
from django.views.decorators.csrf import csrf_protect
from django.views.generic import TemplateView
from django.db import connection
import json


class IndexView(TemplateView):
    """主页类"""
    def get(self, request):
        """get方法, 打开网页时返回所有数据"""
        datas = {
            'types': dict(Articles_type.article_type),
            'pros': self.get_address_data(),
            'girls': self.get_index_data() 
        }
        return render(request, "index.html", datas)
    
    def post(self, request, pro_id=None, city_id=None, type_id=None):
        """post方法，返回请求对应的信息"""
        # TODO 处理请求对应的数据
        if pro_id is None:
            print(pro_id)
        else:
            raise print("pro_id为空")
    
    def get_address_data(self):
        """返回城市数据"""
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

    def get_index_data(self):
        # TODO 优化查询，增加where条件
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


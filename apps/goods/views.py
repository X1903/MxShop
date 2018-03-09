from .serializers import GoodsSerializer
from rest_framework.views import APIView
from rest_framework.response import Response

from .models import Goods

class GoodsListView(APIView):
    """
    列出所有商品
    """
    # def get(self, request, format=None):
    #     goods = Goods.objects.all()[:10]
    #     # 因为前面的是一个列表，加many=True
    #     goods_serializer = GoodsSerializer(goods, many=True)
    #     return Response(goods_serializer.data)

    # def get(self, request, format=None):
    #     goods = Goods.objects.all()[:10]
    #     # 因为前面的是一个列表，加many=True
    #     goods_json = GoodsSerializer(goods, many=True)
    #     return Response(goods_json.data)

    def get(self, request, fromat=None):
        goods = Goods.objects.all()[:10]
        goods_serializer = GoodsSerializer(goods, many=True)
        return Response(goods_serializer.data)
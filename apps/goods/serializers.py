from rest_framework import serializers
from goods.models import Goods, GoodsCategory


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = GoodsCategory
        fields = "__all__"

class GoodsSerializer(serializers.ModelSerializer):
    category = CategorySerializer()

    class Meta:
        model = Goods
        # fields = ('category', 'goods_sn', 'name', 'click_num', 'sold_num', 'market_price')
        fields = "__all__"
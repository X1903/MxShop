# from .serializers import GoodsSerializer
# from rest_framework.views import APIView
# from rest_framework.response import Response
#
# from .models import Goods
#
# class GoodsListView(APIView):
#     """
#     列出所有商品
#     """
#     # def get(self, request, format=None):
#     #     goods = Goods.objects.all()[:10]
#     #     # 因为前面的是一个列表，加many=True
#     #     goods_serializer = GoodsSerializer(goods, many=True)
#     #     return Response(goods_serializer.data)
#
#     # def get(self, request, format=None):
#     #     goods = Goods.objects.all()[:10]
#     #     # 因为前面的是一个列表，加many=True
#     #     goods_json = GoodsSerializer(goods, many=True)
#     #     return Response(goods_json.data)
#
#     def get(self, request, fromat=None):
#         goods = Goods.objects.all()[:10]
#         goods_serializer = GoodsSerializer(goods, many=True)
#         return Response(goods_serializer.data)




# from .models import Goods
# from .serializers import GoodsSerializer
# from rest_framework import mixins
# from rest_framework import generics
# class GoodsListView(mixins.ListModelMixin, generics.GenericAPIView):
#
#     queryset = Goods.objects.all()[:10]
#     serializer_class = GoodsSerializer
#
#     def get(self, request, *args, **kwargs):
#         return self.list(request, *args, **kwargs)


from rest_framework.pagination import PageNumberPagination

class GoodsPagination(PageNumberPagination):
    page_size = 12
    # 向后台要多少条
    page_size_query_param = 'page_size'
    # 定制多少页的参数
    page_query_param = "page"
    max_page_size = 100


# from .models import Goods
# from .serializers import GoodsSerializer
# from rest_framework import generics
# class GoodsListView(generics.ListAPIView):
#     queryset = Goods.objects.all()
#     serializer_class = GoodsSerializer
#     pagination_class = GoodsPagination

# from .models import Goods
# from .serializers import GoodsSerializer
# from rest_framework import mixins
# from rest_framework import viewsets
# class GoodsListViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
#     queryset = Goods.objects.all()
#     pagination_class = GoodsPagination
#     serializer_class = GoodsSerializer


# from .models import Goods
# from .serializers import GoodsSerializer
# from rest_framework import mixins
# from rest_framework import viewsets
# class GoodsListViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
#
#     pagination_class = GoodsPagination
#     serializer_class = GoodsSerializer
#
#     def get_queryset(self):
#         queryset = Goods.objects.all()
#         price_min = self.request.query_params.get('price_min', 0)
#         if price_min:
#             queryset = Goods.objects.filter(shop_price__gt=int(price_min))
#         return queryset

# from .models import Goods
# from .serializers import GoodsSerializer
# from rest_framework import mixins
# from rest_framework import viewsets
# from django_filters.rest_framework import DjangoFilterBackend
# class GoodsListViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
#     queryset = Goods.objects.all()
#     pagination_class = GoodsPagination
#     serializer_class = GoodsSerializer
#     filter_backends = (DjangoFilterBackend,)
#     filter_fields = ('name', 'shop_price')


# from .serializers import GoodsSerializer
# from rest_framework import mixins
# from rest_framework import viewsets
# from django_filters.rest_framework import DjangoFilterBackend
# from .models import Goods
# from .filters import GoodsFilter
# class GoodsListViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
#     queryset = Goods.objects.all()
#     pagination_class = GoodsPagination
#     serializer_class = GoodsSerializer
#     filter_backends = (DjangoFilterBackend,)
#     filter_class = GoodsFilter



from .serializers import GoodsSerializer
from rest_framework import mixins
from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from .models import Goods
from .filters import GoodsFilter

class GoodsListViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    queryset = Goods.objects.all()
    pagination_class = GoodsPagination
    serializer_class = GoodsSerializer
    filter_backends = (DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter)
    filter_class = GoodsFilter
    search_fields = ('name', 'goods_brief', 'goods_desc')
    ordering_fields = ('sold_num', 'add_time')


from .models import GoodsCategory
from .serializers import CategorySerializer
class CategoryViewset(mixins.ListModelMixin, mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    """
    list:
        商品分类列表数据
    retrieve:
        获取商品分类详情
    """
    queryset = GoodsCategory.objects.filter(category_type=1)
    serializer_class = CategorySerializer
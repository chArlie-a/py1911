# Charlie
# date:2020/3/9 10:49
# file_name:serializers
from rest_framework import serializers
from .models import *


class FlowerGoodsSerializer(serializers.ModelSerializer):
    # id = serializers.IntegerField(read_only=True)
    # name = serializers.CharField(max_length=20,min_length=3,error_messages={'max_length':'最多10个字','min_length':'最少3个字'})
    # comment = CommentSerializer(many=True,read_only=True,label='评论')
    # category = CategorySerializer()
    class Meta:
        model = FlowerGoods
        fields = '__all__'

# Charlie
# date:2020/2/26 16:10
# file_name:serializers
from rest_framework import serializers
from .models import *


class CategorySerializer(serializers.ModelSerializer):
    """
    编写针对Category的序列化类
    本类指明了Category的序列化细节
    需要继承ModelSerializer才可以针对模型进行序列化
    在Meta类中 model指明序列化的模型   fields指明序列的字段
    """
    # goods 一定要和 related_name 的值一致

    # StringRelatedField() 可以显示关联模型中的 __str__返回值  many=True 代表多个对象  read_only=True 代表只读
    goods = serializers.StringRelatedField(many=True)

    # goods = serializers.PrimaryKeyRelatedField(many=True,read_only=True)
    # goods = serializers.HyperlinkedRelatedField(read_only=True,many=True,view_name='good-detail')
    class Meta:
        model = Category
        # fields = "__all__"
        fields = ('name', 'goods')


class GoodSerializer(serializers.ModelSerializer):
    class Meta:
        model = Good
        # fields = "__all__"
        fields = ('name', 'desc', 'category')

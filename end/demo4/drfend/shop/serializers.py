# Charlie
# date:2020/2/26 16:10
# file_name:serializers
from rest_framework import serializers
from .models import *


class CustField(serializers.RelatedField):
    """
    自定义序列化类 重写展示方法
    """

    def to_representation(self, value):
        print(value, type(value))
        return str(value.id) + "--" + value.name


class CategorySerializer(serializers.ModelSerializer):
    """
    编写针对Category的序列化类
    本类指明了Category的序列化细节
    需要继承ModelSerializer才可以针对模型进行序列化
    在Meta类中 model指明序列化的模型   fields指明序列的字段
    """
    # goods 一定要和 related_name 的值一致

    # StringRelatedField() 可以显示关联模型中的 __str__返回值  many=True 代表多个对象  read_only=True 代表只读
    # goods = serializers.StringRelatedField(many=True)

    # PrimaryKeyRelatedField 显示主键值
    # goods = serializers.PrimaryKeyRelatedField(many=True,read_only=True)

    # RestFulAPI显示资源
    # goods = serializers.HyperlinkedRelatedField(read_only=True, many=True, view_name='good-detail')

    # 使用自定义序列化类
    # goods = CustField(many=True, read_only=True)
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(max_length=10, min_length=3,
                                 error_messages={'max_length': '最多10个字', 'min_length': '最少3个字'})

    def create(self, validated_data):
        """
        通过重写create方法 来定义模型创建方式
        :param validated_data:
        :return:
        """
        print('重写创建方法', validated_data)
        instance = Category.objects.create(**validated_data)
        print('创建模型实例', instance)
        return instance

    def update(self, instance, validated_data):
        """
        通过重写update，来定义模型的更新方法
        :param instance:来更改之前的实例
        :param validated_data:更改参数
        :return:返回的新实例
        """
        print('重写更新方法', validated_data, instance.name)
        instance.name = validated_data.get('name', instance.name)
        print(instance.name)
        instance.save()

    class Meta:
        model = Category
        # fields = "__all__"
        fields = ('id', 'name')


# class GoodSerializer(serializers.ModelSerializer):
#     category_super = serializers.CharField(source='category.name', read_only=True)


class GoodSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=20, min_length=2, error_messages={
        'max_length': '最多20个字',
        'min_length': '最少2个字'
    })

    category = CategorySerializer(label='分类')

    def validate_category(self, category):
        """
        处理category
        :param validated_data:处理的原始值
        :return: 返回新值
        """

        print('category原始值为', category)
        try:
            Category.objects.get(name=category['name'])
        except:
            raise serializers.ValidationError('输入的分类名不存在')
        return category

    def validate(self, attrs):
        print('收到的数据为', attrs)
        try:
            c = Category.objects.get(name=attrs['category']['name'])
        except:
            c = Category.objects.create(name=attrs['category']['name'])
        attrs['category'] = c
        print('更改之后的数据', attrs)
        return attrs

    def create(self, validated_data):
        print('创建good参数', validated_data)
        instance = Good.objects.create(**validated_data)
        return instance

    def update(self, instance, validated_data):
        print("原始值", instance.name, instance.category)
        instance.name = validated_data.get("name", instance.name)
        instance.category = validated_data.get("category", instance.category)
        instance.save()
        return instance

    class Meta:
        model = Good
        # fields = "__all__"
        fields = ('name', 'desc', 'category', 'category_super')


class GoodImgsSerializer(serializers.Serializer):
    img = serializers.ImageField()
    good = serializers.CharField(source='good.name')

    def validate(self, attrs):
        try:
            g = Good.objects.get(name=attrs['good']['name'])
            print('修改商品', g)
            attrs['good'] = g
        except:
            raise serializers.ValidationError('商品不存在')
        return attrs

    def create(self, validated_data):
        print(validated_data)
        instance = GoodImgs.objects.create(**validated_data)
        return instance

    def update(self, instance, validated_data):
        instance.img = validated_data.get("img", instance.img)
        instance.good = validated_data.get("good", instance.good)
        instance.save()
        return instance

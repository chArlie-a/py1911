# Charlie
# date:2020/3/9 10:49
# file_name:serializers
from rest_framework import serializers
from .models import *


class UserSerializer(serializers.Serializer):
    password = serializers.CharField(write_only=True)
    name = serializers.CharField(max_length=10, min_length=3,
                                 error_messages={'max_length': '最多10个字', 'min_length': '最少3个字'})

    # email = serializers.EmailField(read_only=True, label='邮箱')

    class Meta:
        model = User
        # fields = "__all__"
        exclude = ['user_permissions', 'groups']

    def validate(self, attrs):
        print('原生创建')
        from django.contrib.auth import hashers
        if attrs.get('password'):
            attrs['password'] = hashers.make_password(attrs['password'])
        return attrs


class CommentSerializer(serializers.Serializer):
    commentator = UserSerializer(read_only=True, label='评论人')
    comment_time = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S", read_only=True)
    desc = serializers.CharField(max_length=300, min_length=3,
                                 error_messages={'max_length': '最多300个字', 'min_length': '最少3个字'})

    def create(self, validated_data):
        instance = Category.objects.create(**validated_data)
        return instance


class FlowerGoodsSerializer(serializers.Serializer):
    # id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(max_length=20, min_length=3,
                                 error_messages={'max_length': '最多10个字', 'min_length': '最少3个字'})
    comment = CommentSerializer(many=True, read_only=True, label='评论')
    price = serializers.IntegerField(read_only=True, label='价格')
    distribution = serializers.CharField(max_length=20, min_length=3,
                                         error_messages={'max_length': '最多10个字', 'min_length': '最少3个字'})
    img = serializers.ImageField()
    materials = serializers.CharField(max_length=50, label='材料')

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


class CategorySerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(max_length=10, min_length=3,
                                 error_messages={'max_length': '最多10个字', 'min_length': '最少3个字'})
    img = serializers.ImageField()
    goods = FlowerGoodsSerializer(many=True, read_only=True, label='商品')

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


class TagSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=10, min_length=3,
                                 error_messages={'max_length': '最多10个字', 'min_length': '最少3个字'})
    goods = FlowerGoodsSerializer(many=True, read_only=True, label='商品')

    class Meta:
        model = Tag
        fields = '__all__'


class UserRegistSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=10, min_length=3, error_messages={
        'required': '用户名必填'
    })
    password = serializers.CharField(max_length=10, min_length=3, write_only=True)
    password2 = serializers.CharField(max_length=10, min_length=3, write_only=True)

    def validate_password2(self, data):
        if data != self.initial_data['password']:
            raise serializers.ValidationError('密码不一致')
        else:
            return data

    def create(self, validated_data):
        return User.objects.create_user(username=validated_data.get('username'), email=validated_data.get('email'),
                                        password=validated_data.get('password'))

    # class Meta:
    #     model = FlowerGoods
    #     fields = '__all__'


class CartSerializer(serializers.Serializer):
    goods = FlowerGoodsSerializer(many=True, read_only=True, label='商品')
    user = UserSerializer(read_only=True, label='用户')

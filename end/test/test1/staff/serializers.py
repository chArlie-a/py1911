# Charlie
# date:2020/3/2 10:40
# file_name:serializers
from rest_framework import serializers
from .models import *


class DepartmentSerializer(serializers.ModelSerializer):
    def create(self, validated_data):
        """
        通过重写create方法 来定义模型创建方式
        :param validated_data:
        :return:
        """
        print('重写创建方法', validated_data)
        instance = Department.objects.create(**validated_data)
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
        model = Department
        # fields = "__all__"
        fields = ('id', 'name')


class StaffSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=20, min_length=2, error_messages={
        'max_length': '最多20个字',
        'min_length': '最少2个字'
    })

    department = DepartmentSerializer(label='部门')

    def validate_category(self, department):
        """
        处理category
        :param validated_data:处理的原始值
        :return: 返回新值
        """

        print('category原始值为', department)
        try:
            Department.objects.get(name=department['name'])
        except:
            raise serializers.ValidationError('输入的部门名不存在')
        return department

    def validate(self, attrs):
        print('收到的数据为', attrs)
        try:
            c = Department.objects.get(name=attrs['department']['name'])
        except:
            c = Department.objects.create(name=attrs['department']['name'])
        attrs['category'] = c
        print('更改之后的数据', attrs)
        return attrs

    def create(self, validated_data):
        print('创建good参数', validated_data)
        instance = Staff.objects.create(**validated_data)
        return instance

    def update(self, instance, validated_data):
        print("原始值", instance.name, instance.department)
        instance.name = validated_data.get("name", instance.name)
        instance.department = validated_data.get("department", instance.department)
        instance.save()
        return instance

    class Meta:
        model = Staff
        # fields = "__all__"
        fields = ('name', 'department', 'department_super')

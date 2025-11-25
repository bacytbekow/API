from rest_framework import serializers,generics
from rest_framework.renderers import JSONRenderer
from .models import Women,Category
# class WomenModel:
#     def __init__(self,title,content):
#         self.title = title
#         self.content = content

class WomenSerializer(serializers.ModelSerializer):
    # user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    class Meta:
        model = Women
        fields = "__all__"

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ["name"]
    # title = serializers.CharField(max_length=255)
    # content = serializers.CharField()
    # cat = serializers.PrimaryKeyRelatedField(queryset=Category.objects.all())


    # def create(self, validated_data):
    #     return Women.objects.create(**validated_data)
    #
    # def update(self, instance, validated_data):
    #     instance.title = validated_data.get('title', instance.title)
    #     instance.content = validated_data.get('content', instance.content)
    #     instance.cat = validated_data.get('cat', instance.cat)
    #
    #     return instance
# def encode():
#     model = WomenModel('Andjelina Jolie','Content: Angelina Jolie')
#     model_str = WomenSerializer(model)
#     print(model_str.data,type(model_str.data),sep='\n')
#
#     json = JSONRenderer().render(model_str.data)
#     print(json)
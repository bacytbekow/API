
from django.shortcuts import render
from .serializers import WomenSerializer, CategorySerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Women, Category
from rest_framework import generics
from rest_framework import viewsets
from rest_framework import mixins
from rest_framework.viewsets import GenericViewSet
# Create your views here.


class WomenAPIViewSet(viewsets.mixins.CreateModelMixin,
                   mixins.RetrieveModelMixin,
                   mixins.UpdateModelMixin,
                   mixins.DestroyModelMixin,
                   mixins.ListModelMixin,
                   GenericViewSet):   #// ModelViewSet
    queryset = Women.objects.all()
    serializer_class = WomenSerializer

class CategoryAPIViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer





# class WomenAPIList(generics.ListCreateAPIView):
#     queryset = Women.objects.all()
#     serializer_class = WomenSerializer
#
# class WomenAPIUpdate(generics.UpdateAPIView):
#     queryset = Women.objects.all()
#     serializer_class = WomenSerializer
#
# class WomenDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Women.objects.all()
#     serializer_class = WomenSerializer

#
# class WomenAPIView(APIView):
#     def get(self, request):
#         w = Women.objects.all()
#         return Response({'posts': WomenSerializer(w, many=True).data})
#
#
#     def post(self, request):
#         serializer = WomenSerializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#
#         # post_new = Women.objects.create(
#         #     title=request.data['title'],
#         #     content=request.data['content'],
#         #     cat_id=request.data['cat']
#         # )
#
#         serializer.save()
#         return Response({'posts': serializer.data})
#
#
#     def put(self,request, *args, **kwargs):
#         pk = kwargs.get("pk", None)
#         if not pk:
#             return Response({"error": "Method PUT not allowed"})
#
#
#         try:
#             instance = Women.objects.get(pk=pk)
#
#         except:
#             return Response({"error": "Object does not exists"})
#
#         serializer = WomenSerializer(data=request, instance=instance)
#         serializer.is_valid()
#         serializer.save()
#
#         return Response({"post": serializer.data})
#

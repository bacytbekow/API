from django.shortcuts import render
from .serializers import WomenSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Women
from rest_framework import generics
from rest_framework import viewsets
# Create your views here.


class WomenAPIViewSet(viewsets.ModelViewSet):
    queryset = Women.objects.all()
    serializer_class = WomenSerializer





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

import djoser
from django.contrib import admin
from django.urls import path, include,re_path
from api.views import *
from rest_framework import routers

from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView
# router = routers.DefaultRouter()
# router.register(r'women', WomenAPIViewSet, basename='women')
# print(router.urls)
# router.register(r'category', CategoryAPIViewSet)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/drf-auth/', include("rest_framework.urls")),

    path('api/v1/auth/', include("djoser.urls")),
    re_path(r'^auth/', include('djoser.urls.authtoken')),

    # path('api/', include(router.urls)),
    path('api/v1/women/', WomenAPIList.as_view()),
    path('api/v1/women/<int:pk>/', WomenAPIUpdate.as_view()),
    path('api/v1/womendelete/<int:pk>/', WomenDestroyAPIView.as_view()),


    path('api/v1/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/v1/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/v1/token/verify/', TokenVerifyView.as_view(), name='token_verify'),

    # path('api/womenlist/', WomenAPIList.as_view(), name='women_list'),
    # # path('api/womenlist/<int:pk>/', WomenAPIList.as_view())
    # path('api/womenlist/<int:pk>/', WomenAPIUpdate.as_view()),
    # path('api/womendetail/<int:pk>/', WomenDetailAPIView.as_view())
    # path('api/womenlist/', WomenAPIViewSet.as_view({'get': 'list'})),
    # path('api/womenlist/<int:pk>/', WomenAPIViewSet.as_view({'put': 'update'}))
]

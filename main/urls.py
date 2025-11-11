
from django.contrib import admin
from django.urls import path, include
from api.views import *
from rest_framework import routers

router = routers.SimpleRouter()
router.register(r'women', WomenAPIViewSet)
urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls))
    # path('api/womenlist/', WomenAPIList.as_view(), name='women_list'),
    # # path('api/womenlist/<int:pk>/', WomenAPIList.as_view())
    # path('api/womenlist/<int:pk>/', WomenAPIUpdate.as_view()),
    # path('api/womendetail/<int:pk>/', WomenDetailAPIView.as_view())
    # path('api/womenlist/', WomenAPIViewSet.as_view({'get': 'list'})),
    # path('api/womenlist/<int:pk>/', WomenAPIViewSet.as_view({'put': 'update'}))
]
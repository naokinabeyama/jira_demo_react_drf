from django.urls import path, include
from rest_framework import routers, urlpatterns

router = routers.DefaultRouter()

urlpatterns = [
    path('', include(router.urls)),
]
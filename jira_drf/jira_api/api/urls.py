from django.urls import path, include
from rest_framework import routers
from .views import TaskViewSet, CategoryViewSet, ListUserView, LoginUserView, ProfileVIewSet, CreateUserView

# ModelViewSetで継承したものはrouterに
# genericsを継承したものはpathを記述する

router = routers.DefaultRouter()
router.register('category', CategoryViewSet)
router.register('tasks', TaskViewSet)
router.register('profile', ProfileVIewSet)

urlpatterns = [
    path('create/', CreateUserView.as_view(), name='create'),
    path('users/', ListUserView.as_view(), name='users'),
    path('loginuser/', LoginUserView.as_view(), name='loginuser'),
    path('', include(router.urls)),
]

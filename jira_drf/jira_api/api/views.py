from django.http import request, response
from django.shortcuts import render
from rest_framework import serializers, status, permissions, generics, viewsets
from .serializers import UserSerializer, CategorySerializer, TaskSerializer, ProfileSerializer
from rest_framework.response import Response
from .models import Task, Profile, Category
from django.contrib.auth.models import User
from . import custompermissions

# generics.○○は特化している場合(createAPIViewなら作成だけ)
# viewsets.ModelViewSetはCRUD全般使用可能


class CreateUserView(generics.CreateAPIView):
    serializer_class = UserSerializer
    # settings.pyでjwt(認証)の設定をしているためpermissions.AllowAnyで新規作成は認証がなくても作成できるようにしている
    permission_classes = (permissions.AllowAny,)


class ListUserView(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


# RetrieveUpdateAPIVIew 特定のオブジェクトを検索して返してくれる
class LoginUserView(generics.RetrieveUpdateAPIView):
    serializer_class = UserSerializer

    # ログインユーザーを返す
    def get_object(self):
        # request.user == ログインしているユーザー
        return self.request.user

    # 使わないCRUDをアクセスできないようにする
    def update(self, request, *args, **kwargs):
        response = {'message': 'PUT method is not allowed'}
        return Response(response, status=status.HTTP_400_BAD_REQUEST)


class ProfileVIewSet(viewsets.ModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer

    def perform_create(self, serializer):
        serializer.save(user_profile=self.request.user)
    
    # 使わないCRUDをアクセスできないようにする
    # delete
    def destroy(self, request, *args, **kwargs):
        response = {'message': 'DELETE method is not allowed'}
        return Response(response, status=status.HTTP_400_BAD_REQUEST)
    # update
    def partial_update(self, request, *args, **kwargs):
        response = {'message': 'PATCH method is not allowed'}
        return Response(response, status=status.HTTP_400_BAD_REQUEST)


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

    # 使わないCRUDをアクセスできないようにする
    # delete
    def destroy(self, request, *args, **kwargs):
        response = {'message': 'DELETE method is not allowed'}
        return Response(response, status=status.HTTP_400_BAD_REQUEST)
    # update
    def update(self, request, *args, **kwargs):
        response = {'message': 'PUT method is not allowed'}
        return Response(response, status=status.HTTP_400_BAD_REQUEST)
    # update
    def partial_update(self, request, *args, **kwargs):
        response = {'message': 'PATCH method is not allowed'}
        return Response(response, status=status.HTTP_400_BAD_REQUEST)


class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    # custompermissions.OwnerPermissionに上書きする
    permission_classes = (permissions.IsAuthenticated, custompermissions.OwnerPermission,)

    # 新規で作成したらログインユーザーが自動でownerに
    def perform_create(self, serializer):
        print(self.request.user)
        serializer.save(owner=self.request.user)

    # 使わないCRUDをアクセスできないようにする
    def partial_update(self, request, *args, **kwargs):
        response = {'message': 'PATCH method is not allowed'}
        return Response(response, status=status.HTTP_400_BAD_REQUEST)


from rest_framework import serializers
from .models import Task, Profile, Category
from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'password']
        # extra_kwargs fieldsに対してオプションを付けることができる
        # write_only True 読み取り不可, required True 必須
        extra_kwargs = {'password':{'write_only': True, 'required': True}}

    # パスワードのハッシュ化 (create_user(**validated_data)でハッシュ化しuserをデータベースへ)
    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ['id', 'user_profile', 'img']
        extra_kwargs = {'user_profile':{'read_only': True}}


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'item']
        

class TaskSerializer(serializers.ModelSerializer):
        # ForeignKeyで参照している値　直接参照
        # reactでidだけでなく名前も取得したい
        category_item = serializers.ReadOnlyField(source='category.item', read_only=True)

        owner_username = serializers.ReadOnlyField(source='owner.username', read_only=True)

        responsible_username = serializers.ReadOnlyField(source='responsible.username', read_only=True)

        # statusはchoices key,value両方取得したい(react)
        # [get_choicesで参照(STATUSを小文字に)_display]を設定するとvalueが取得できる
        status_name = serializers.CharField(source='get_status_display', read_only=True)
        
        # 作成日時
        created_at = serializers.DateTimeField(format='%Y-%m-%d %H:%M', read_only=True)
        # 更新日時
        updated_at = serializers.DateTimeField(format='%Y-%m-%d %H:%M', read_only=True)


        class Meta:
            model = Task
            fields = ['id', 'task', 'description', 'criteria', 'status', 'status_name', 'category', 'category_item', 'estimate', 'owner', 'owner_username', 'responsible', 'responsible_username', 'created_at', 'updated_at']
            extra_kwargs = {'owner': {'read_only': True}}

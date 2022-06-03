from django.core import validators
from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator
import uuid


def upload_avatar_path(instance, filename):
    # 拡張子(jpeg, pingなど)を代入
    ext = filename.split('.')[-1]
    # media/avatarsに画像を保存する
    return '/'.join(['avatars', str(instance.user_profile.id)+str('.')+str(ext)])


# ユーザープロフィール
class Profile(models.Model):
    # Userと一対一で紐付け
    user_profile = models.OneToOneField(
        User, related_name='user_profile',
        on_delete=models.CASCADE 
    )

    # アバター画像
    # upload = アバター画像の保存先
    img = models.ImageField(blank=True, null=True, upload_to=upload_avatar_path)

    def __str__(self):
        return self.user_profile.username


# カテゴリー
class Category(models.Model):
    item = models.CharField(max_length=100)

    def __str__(self):
        return self.item


# タスク
class Task(models.Model):
    STATUS = (
        ('1', 'Not started'),
        ('2', 'On going'),
        ('3', 'Done'),
    )
    
    # id
    # editable = False 編集不可
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
    # タイトル
    task = models.CharField(max_length=100)
    # 説明
    description = models.CharField(max_length=300)
    # 基準
    criteria = models.CharField(max_length=100)
    # ステータス
    status = models.CharField(max_length=40, choices=STATUS, default='1')
    # カテゴリー(カテゴリーモデルから参照)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    # 見込み (0以上の整数)
    estimate = models.IntegerField(validators=[MinValueValidator(0)])
    # オーナー (DjangoのUserモデルと紐付け)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='owner')
    # タスクを行う人 (DjangoのUserモデルと紐付け)
    responsible = models.ForeignKey(User, on_delete=models.CASCADE, related_name='responsible')
    # 作成日時 (auto_now_add 作成された日時を自動で登録)
    created_at = models.DateTimeField(auto_now_add=True)
    # 更新日時 (auto_now 更新するたびに更新してくれる)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.task


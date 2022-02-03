import pytz
from datetime import datetime
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db import models


# 현재 시각을 반환하는 함수
def get_current_time():
    return datetime.now(pytz.timezone('Asia/Seoul')).replace(tzinfo=None)


class TimeStampedModel(models.Model):
    created_at = models.DateTimeField(default=get_current_time)
    updated_at = models.DateTimeField(default=get_current_time)

    class Meta:
        abstract = True

    def save(self, *args, **kwargs):
        self.updated_at = get_current_time()
        super().save(*args, **kwargs)


class UserManager(BaseUserManager):
    def create_user(self, user_id, password=None, **extra_fields):
        try:
            user = self.model(
                user_id=user_id,
                **extra_fields
            )
            user.set_password(password)
            user.save()
            return user
        except Exception as e:
            print(e)

    def create_superuser(self, user_id, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        if extra_fields.get('is_superuser') is not True or extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True && is_superuser=True')
        return self.create_user(user_id, password, **extra_fields)


class User(AbstractBaseUser, TimeStampedModel, PermissionsMixin):
    user_id = models.BigIntegerField('회원번호', primary_key=True)
    nickname = models.CharField('닉네임', max_length=20, unique=True)
    acc_percent = models.FloatField('적중률', default=0.0)
    point = models.IntegerField('고래밥', default=100)
    profile_img = models.URLField('프로필 url', null=True)
    is_default_profile = models.BooleanField('기본 프로필 여부', default=True)

    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    USERNAME_FIELD = 'user_id'
    REQUIRED_FIELDS = ['nickname']

    objects = UserManager()

    def __str__(self):
        return self.nickname

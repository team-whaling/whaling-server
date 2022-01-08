from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db import models


class TimeStampedModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class UserManager(BaseUserManager):
    def create_user(self, user_id, email, password=None, **extra_fields):
        try:
            user = self.model(
                user_id=user_id,
                email=self.normalize_email(email),
                **extra_fields
            )
            user.set_password(password)
            user.save()
            return user
        except Exception as e:
            print(e)

    def create_superuser(self, user_id, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        if extra_fields.get('is_superuser') is not True or extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True && is_superuser=True')
        return self.create_user(user_id, email, password, **extra_fields)


class User(AbstractBaseUser, TimeStampedModel, PermissionsMixin):
    user_id = models.BigIntegerField(primary_key=True)  # 카카오 회원 번호로 설정
    email = models.EmailField(unique=True)
    nickname = models.CharField(max_length=20, unique=True)
    acc_percent = models.FloatField('적중률', default=0.0)
    point = models.IntegerField('고래밥', default=100)
    profile_img = models.URLField('프로필 url', null=True)
    is_default_profile = models.BooleanField('기본 프로필 여부', default=True)

    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['user_id', 'nickname']

    objects = UserManager()

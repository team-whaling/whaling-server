from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import *

router = DefaultRouter()
router.register(r'users', UserViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('auth', kakao_login),

    # 테스트용
    path('kakao/login', KakaoLoginRedirectTestView.as_view()),
    path('kakao/login/callback', KakaoLoginRequestTestView.as_view()),
]

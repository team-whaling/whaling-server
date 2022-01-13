from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenRefreshView, TokenVerifyView

from .views import *

router = DefaultRouter()
router.register(r'users', UserViewSet)

urlpatterns = [
    # 로그인/회원가입
    path('auth', kakao_login),

    # 토큰 재발급 및 검증
    path('token/refresh', TokenRefreshView.as_view()),
    path('token/verify', TokenVerifyView.as_view()),

    # 테스트용
    path('', include(router.urls)),
    path('auth/kakao', KakaoLoginRedirectTestView.as_view()),
    path('auth/kakao/callback', KakaoLoginRequestTestView.as_view()),
]

from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenRefreshView

from account.views import UserViewSet, kakao_login, TokenVerifyView

router = DefaultRouter()
router.register(r'user', UserViewSet, basename='user')

urlpatterns = [
    # 로그인/회원가입
    path('auth', kakao_login),
    # 토큰 재발급 및 검증
    path('auth/token/refresh', TokenRefreshView.as_view()),
    path('auth/token/verify', TokenVerifyView.as_view()),
    # 유저
    path('', include(router.urls)),
]

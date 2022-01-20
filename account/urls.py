from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenRefreshView, TokenVerifyView

from .views import auth_views, user_views

router = DefaultRouter()
router.register(r'user', user_views.UserViewSet, basename='user')

urlpatterns = [
    # 로그인/회원가입
    path('auth', auth_views.kakao_login),

    # 토큰 재발급 및 검증
    path('auth/token/refresh', TokenRefreshView.as_view()),
    path('auth/token/verify', TokenVerifyView.as_view()),

    # 테스트용
    path('', include(router.urls)),
    path('auth/kakao', auth_views.KakaoLoginRedirectTestView.as_view()),
    path('auth/kakao/callback', auth_views.KakaoLoginRequestTestView.as_view()),
]

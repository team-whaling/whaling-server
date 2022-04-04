from account.views import UserViewSet, kakao_login, TokenViewSet
from django.urls import path, include
from rest_framework.routers import DefaultRouter

router = DefaultRouter(trailing_slash=False)
router.register(r'user', UserViewSet, basename='user')
router.register(r'auth/token', TokenViewSet, basename='token')
router_with_slash = DefaultRouter(trailing_slash=True)
router_with_slash.register(r'user', UserViewSet, basename='user')
router_with_slash.register(r'auth/token', TokenViewSet, basename='token')

urlpatterns = [
    # 로그인/회원가입
    path('auth', kakao_login),
    # 토큰 및 유저
    path('', include(router.urls)),
    path('', include(router_with_slash.urls)),
]

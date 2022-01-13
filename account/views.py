import json

import environ
import requests
from django.contrib.auth import get_user_model
from django.http import HttpResponseRedirect
from django.views import View
from rest_framework import viewsets, status, generics
from rest_framework.decorators import permission_classes, api_view
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken

from .serializers import UserSerializer

env = environ.Env()
environ.Env.read_env()

User = get_user_model()


# 카카오 로그인 테스트용 리다이렉트 뷰
@permission_classes([AllowAny])
class KakaoLoginRedirectTestView(View):
    def get(self, request):
        app_key = env('KAKAO_REST_API_KEY')
        redirect_uri = 'http://127.0.0.1:8000/account/auth/kakao/callback'
        base_url = 'https://kauth.kakao.com/oauth/authorize?response_type=code'
        return HttpResponseRedirect(f'{base_url}&client_id={app_key}&redirect_uri={redirect_uri}')


# 카카오 로그인 테스트용 리퀘스트 뷰
@permission_classes([AllowAny])
class KakaoLoginRequestTestView(generics.GenericAPIView):
    def get(self, request):
        # 인가 코드 에러 처리
        error_desc = request.GET.get('error_description', None)
        if error_desc is not None:
            return Response(error_desc, status=status.HTTP_400_BAD_REQUEST)

        # 사용자 인증 API에 POST 요청
        auth_code = request.GET.get('code', None)
        redirect_uri = 'http://127.0.0.1:8000/account/auth/kakao/callback'
        uri = 'http://127.0.0.1:8000/account/auth'
        data = {
            'code': auth_code,
            'redirect_uri': redirect_uri
        }
        # response = requests.post(uri, data=data)
        return Response(data)


# JWT 발급 함수
def get_tokens_for_user(user):
    refresh = RefreshToken.for_user(user)

    return {
        'refresh_token': str(refresh),
        'access_token': str(refresh.access_token),
    }


# 소셜 로그인 및 회원가입 뷰
@api_view(['POST'])
@permission_classes([AllowAny])
def kakao_login(request):
    # 액세스 토큰 발급용 Request
    request_body = json.loads(request.body)
    auth_code = request_body.get('code', None)
    redirect_uri = request_body.get('redirect_uri', None)
    kakao_token_url = 'https://kauth.kakao.com/oauth/token'
    headers = {'Content-type': 'application/x-www-form-urlencoded;charset=utf-8'}
    data = {
        'grant_type': 'authorization_code',
        'client_id': env('KAKAO_REST_API_KEY'),
        'redirect_uri': redirect_uri,
        'code': auth_code,
        'client_secret': env('KAKAO_CLIENT_SECRET')
    }
    # 카카오로부터 액세스 토큰 받기
    kakao_token_response = requests.post(kakao_token_url, headers=headers, data=data).json()
    access_token = kakao_token_response.get('access_token')

    # 사용자 정보 접근용 Request
    kakao_api_url = 'https://kapi.kakao.com/v2/user/me'
    headers = {
        'Content-type': 'application/x-www-form-urlencoded;charset=utf-8',
        'Authorization': f'Bearer {access_token}'
    }
    # 카카오로부터 사용자 정보 받기
    kakao_api_response = requests.post(kakao_api_url, headers=headers).json()
    user_id = kakao_api_response.get('id')

    # 카카오 API 응답에 에러가 있다면
    if user_id is None:
        return Response(kakao_api_response, status=status.HTTP_400_BAD_REQUEST)

    try:
        # 기존에 가입한 유저인 경우, 유저 정보를 불러옴
        user = User.objects.get(user_id=user_id)
        http_status = status.HTTP_201_CREATED
    except User.DoesNotExist:
        # 새로 가입하는 유저인 경우, 유저를 새로 생성함
        user_profile = kakao_api_response.get('kakao_account').get('profile')
        user_data = {
            'user_id': user_id,
            'nickname': f'user{user_id}',
            'profile_img': user_profile.get('profile_image_url'),
            'is_default_profile': user_profile.get('is_default_image')
        }
        serializer = UserSerializer(data=user_data)
        if not serializer.is_valid(raise_exception=True):
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        user = serializer.save()
        http_status = status.HTTP_201_CREATED

    # 유저 정보 및 JWT 응답
    response = {
        'user': {
            'nickname': user.nickname
        },
        'token': get_tokens_for_user(user)
    }
    return Response(response, status=http_status)


class UserViewSet(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()

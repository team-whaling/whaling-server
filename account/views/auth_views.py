import json
import requests
from django.contrib.auth import get_user_model
from django.http import HttpResponseRedirect
from django.views import View
from rest_framework import status, generics
from rest_framework.decorators import permission_classes, api_view
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken

from whaling.settings import env

from account.serializers import UserAuthSerializer

redirect_uri = 'https://whaling.co.kr/auth/kakao/callback'

User = get_user_model()


# 카카오 로그인 테스트용 리다이렉트 뷰
@permission_classes([AllowAny])
class KakaoLoginRedirectTestView(View):
    def get(self, request):
        app_key = env('KAKAO_REST_API_KEY')
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
        uri = 'https://whaling.co.kr/auth'
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

    # 카카오 API 응답에 에러가 있다면 에러 리턴
    if user_id is None:
        return Response(kakao_api_response, status=status.HTTP_400_BAD_REQUEST)

    user_profile = kakao_api_response.get('kakao_account').get('profile')
    user_data = {
        'user_id': user_id,
        'nickname': f'user{user_id}',
        'profile_img': user_profile.get('profile_image_url'),
        'is_default_profile': user_profile.get('is_default_image')
    }

    try:
        # 기존에 가입한 유저인 경우, 유저 업데이트
        user = User.objects.get(user_id=user_id)
        user_data['nickname'] = user.nickname
        serializer = UserAuthSerializer(user, data=user_data)
        http_status = status.HTTP_200_OK
    except User.DoesNotExist:
        # 새로 가입하는 유저인 경우, 유저 생성
        serializer = UserAuthSerializer(data=user_data)
        http_status = status.HTTP_201_CREATED

    serializer.is_valid(raise_exception=True)
    user = serializer.save()

    # 유저 정보 및 JWT 응답
    response = {
        'user': {
            'nickname': user.nickname
        },
        'token': get_tokens_for_user(user)
    }
    return Response(response, status=http_status)

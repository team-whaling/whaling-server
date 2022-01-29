import json
import requests
from django.contrib.auth import get_user_model
from rest_framework import status
from rest_framework.decorators import permission_classes, api_view, action
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet
from rest_framework_simplejwt.exceptions import TokenError
from rest_framework_simplejwt.serializers import TokenVerifySerializer
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.authentication import JWTAuthentication

from whaling.settings import env

from account.serializers import UserAuthSerializer, RefreshTokenSerializer

User = get_user_model()


# JWT 발급 함수
def get_tokens_for_user(user):
    refresh = RefreshToken.for_user(user)

    return {
        'access_token': str(refresh.access_token),
        'refresh_token': str(refresh)
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
    if access_token is None:
        return Response(kakao_token_response, status=status.HTTP_400_BAD_REQUEST)

    # 사용자 정보 접근용 Request
    kakao_api_url = 'https://kapi.kakao.com/v2/user/me'
    headers = {
        'Content-type': 'application/x-www-form-urlencoded;charset=utf-8',
        'Authorization': f'Bearer {access_token}'
    }
    # 카카오로부터 사용자 정보 받기
    kakao_api_response = requests.post(kakao_api_url, headers=headers).json()
    user_id = kakao_api_response.get('id')
    if user_id is None:
        return Response(kakao_api_response, status=status.HTTP_400_BAD_REQUEST)

    user_data = {
        'user_id': user_id,
        'nickname': f'user{user_id}'
    }
    # 프로필 이미지 접근에 동의한 유저의 정보만 저장
    user_profile = kakao_api_response.get('kakao_account').get('profile', None)
    if user_profile is not None:
        user_data['profile_img'] = user_profile.get('profile_image_url')
        user_data['is_default_profile'] = user_profile.get('is_default_image')

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


class TokenViewSet(ViewSet):
    permission_classes = [AllowAny]
    authentication_classes = []

    @action(methods=['post'], detail=False)
    def verify(self, request):
        jwt = JWTAuthentication()
        header = jwt.get_header(request)
        if header is None:
            return Response({'message': '헤더에 토큰이 없습니다.'}, status=status.HTTP_400_BAD_REQUEST)
        data = {
            'token': str(jwt.get_raw_token(header), 'utf-8')
        }
        serializer = TokenVerifySerializer(data=data)
        try:
            serializer.is_valid(raise_exception=True)
        except:
            return Response({'message': '만료된 혹은 유효하지 않은 액세스 토큰입니다.'}, status=status.HTTP_401_UNAUTHORIZED)
        return Response(status=status.HTTP_200_OK)

    @action(methods=['post'], detail=False)
    def refresh(self, request):
        serializer = RefreshTokenSerializer(data=request.data)
        try:
            serializer.is_valid(raise_exception=True)
        except TokenError:
            return Response({'message': '만료된 혹은 유효하지 않은 리프레시 토큰입니다.'}, status=status.HTTP_401_UNAUTHORIZED)
        return Response(serializer.validated_data, status=status.HTTP_200_OK)

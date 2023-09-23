from django.core.exceptions import ObjectDoesNotExist
from rest_framework.authentication import BaseAuthentication
import jwt
from rest_framework.exceptions import AuthenticationFailed
import re
from config.config import JConfig as MainConfig
from xj_user.models import User

config = MainConfig()


class CustomJWTAuthentication(BaseAuthentication):

    def authenticate(self, request):
        token = request.META.get('HTTP_AUTHORIZATION', '')
        if not token:
            raise AuthenticationFailed('请登录')  # 缺少Token

        token_parts = token.split(' ')
        if len(token_parts) != 2 or token_parts[0].lower() != 'bearer':
            raise AuthenticationFailed('无效的Token')

        token = token_parts[1]

        try:
            decoded_token = jwt.decode(token, key=config.get('xj_user', 'JWT_SECRET_KEY', '@zxmxy2021!'),
                                       verify=True, algorithms=["RS256", "HS256"])
            user_id = decoded_token['user_id']
            # 根据user_id获取对应的用户对象
            try:
                user = User.objects.get(id=user_id)
            except User.DoesNotExist:
                raise AuthenticationFailed('用户不存在')
            return (user, None)
        except jwt.ExpiredSignatureError:
            raise AuthenticationFailed('Token已过期')
        except jwt.InvalidTokenError:
            raise AuthenticationFailed('无效的Token')

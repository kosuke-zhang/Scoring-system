"""cxy URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from rest_framework import serializers
from rest_framework.documentation import include_docs_urls
from rest_framework.exceptions import AuthenticationFailed
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
)

from competition.views import CompetitionViewSet
from composition.views import CompositionViewSet
from grade.views import GradeViewSet
from user.views import UserViewSet
from utils.MyBackend import AuthBackend

router = routers.DefaultRouter()
router.register('api/competition', CompetitionViewSet)
router.register('api/composition', CompositionViewSet)
router.register('api/grade', GradeViewSet)
router.register('api/user', UserViewSet)


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    def __init__(self, *args, **kwargs):
        serializers.Serializer.__init__(self, *args, **kwargs)

        self.fields[self.username_field] = serializers.CharField()
        # self.fields['password'] = PasswordField()

    def validate(self, attrs):
        self.user = AuthBackend().authenticate(None, attrs[self.username_field], None)
        # or not self.user.is_active
        if self.user is None:
            raise AuthenticationFailed('密码错误，请重新输入。')

        data = {}

        refresh = self.get_token(self.user)

        data['access'] = str(refresh.access_token)

        return data


class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer


urlpatterns = [
    # path('', include(urls)),
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('doc/', include_docs_urls(title='文档')),
    path('api/token/', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    # path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]

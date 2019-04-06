from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet

from .models import CompetitionModel
from .serializer import CompetitionSerializer


class CompetitionViewSet(ModelViewSet):
    queryset = CompetitionModel.objects.all()
    serializer_class = CompetitionSerializer
    permission_classes = (IsAuthenticated,)


class ListCompetition(APIView):
    """
    列出系统中的所有用户

    * 需要 token 认证。
    * 只有 admin 用户才能访问此视图。
    """

    permission_classes = (AllowAny,)

    def get(self, request, format=None):
        """
        Return a list of all users.
        """
        competitions = CompetitionModel.objects.all()
        competitions = list(competitions.values())

        return Response(competitions)

from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet

from .models import CompetitionModel
from .serializer import CompetitionSerializer


class CompetitionViewSet(ModelViewSet):
    queryset = CompetitionModel.objects.all()
    serializer_class = CompetitionSerializer
    permission_classes = (IsAuthenticated,)

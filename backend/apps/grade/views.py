from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet

from .models import GradeModel
from .serializer import GradeSerializer


class GradeViewSet(ModelViewSet):
    queryset = GradeModel.objects.all()
    serializer_class = GradeSerializer
    permission_classes = (IsAuthenticated,)

from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet

from composition.serializer import CompositionSerializer
from .models import CompositionModel


class CompositionViewSet(ModelViewSet):
    queryset = CompositionModel.objects.all()
    serializer_class = CompositionSerializer
    permission_classes = (IsAuthenticated,)

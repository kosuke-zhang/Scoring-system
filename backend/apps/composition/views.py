from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet

from composition.serializer import CompositionSerializer, ListCompositionSerializer
from .models import CompositionModel


class CompositionViewSet(ModelViewSet):
    queryset = CompositionModel.objects.all()
    serializer_class = CompositionSerializer
    permission_classes = (IsAuthenticated,)

    def list(self, request, *args, **kwargs):
        competition = request.query_params.get('competition', None)
        competition = int(competition)
        queryset = self.filter_queryset(self.get_queryset())

        queryset = queryset.filter(competition=competition)

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)

        return Response(serializer.data)


class ListComposition(ModelViewSet):
    queryset = CompositionModel.objects.all()
    serializer_class = ListCompositionSerializer
    permission_classes = (AllowAny,)

    def list(self, request, *args, **kwargs):
        competition = request.query_params.get('competition', None)
        competition = int(competition)
        queryset = self.filter_queryset(self.get_queryset())

        queryset = queryset.filter(competition=competition)

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)

        results = sorted(serializer.data, key=lambda x: x['score_amount'], reverse=True)

        return Response(results)

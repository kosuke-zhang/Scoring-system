from rest_framework import response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet

from .models import GradeModel
from .serializer import GradeSerializer


class GradeViewSet(ModelViewSet):
    queryset = GradeModel.objects.all()
    serializer_class = GradeSerializer
    permission_classes = (IsAuthenticated,)

    def create(self, request, *args, **kwargs):
        request.data['judger'] = request.user.id
        grade = GradeModel.objects.filter(judger=request.data['judger'], composition=request.data['composition'])
        if grade.exists():
            return response.Response({'message': '成绩一旦提交不能更改！'}, status=status.HTTP_400_BAD_REQUEST)
        data = super().create(request, *args, **kwargs)
        return data

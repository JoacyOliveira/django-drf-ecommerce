from rest_framework import viewsets
from rest_framework.response import Response
from drf_spectacular.utils import extend_schema
from .models import Category
from .serializers import CategorySerializer

# Create your views here.


class CategoryViewSet(viewsets.ViewSet):
    "Simple Viewset for viewing all categoies"

    queryset = Category.objects.all()

    @extend_schema(responses=CategorySerializer)
    def list(self, request):
        serializer = CategorySerializer(self.queryset, many=True)
        return Response(serializer.data)


from rest_framework import generics
from Detail.models import Detail
from .serializers import DetailSerializer
class DetailAPIView(generics.ListAPIView):
    queryset = Detail.objects.all()
    serializer_class = DetailSerializer
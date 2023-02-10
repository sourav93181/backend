from django.views.generic import ListView
from rest_framework import generics
from .models import Detail
from api.serializers import DetailSerializer
class DetailListView(ListView):
    model = Detail
    template_name = 'book_list.html'

class DetailSingleView(generics.RetrieveAPIView):
    queryset = Detail.objects.all()
    serializer_class = DetailSerializer

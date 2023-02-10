from django.urls import path
from .views import DetailAPIView
from Detail.views import DetailSingleView
from . import views
urlpatterns = [
path('', DetailAPIView.as_view()),
path('<int:pk>/', DetailSingleView.as_view()),
]
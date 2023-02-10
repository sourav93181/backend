from django.urls import path
from .views import DetailListView,DetailSingleView
from . import views
urlpatterns = [
path('', DetailListView.as_view(), name='home'),
path('<int:pk>/', DetailSingleView.as_view()),
]
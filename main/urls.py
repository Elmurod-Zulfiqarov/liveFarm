from django.urls import path

from .views import PetListView, PetDetailView, MilkListView, MilkDetailView, FodderListView, FodderDetailView

urlpatterns = [
    path('pet/', PetListView.as_view()),
    path('pet/<int:pk>/', PetDetailView.as_view()),
    path('milk/', MilkListView.as_view()),
    path('milk/<int:pk>/', MilkDetailView.as_view()),
    path('fodder/', FodderListView.as_view()),
    path('fodder/<int:pk>/', FodderDetailView.as_view()),
]


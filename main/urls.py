from posixpath import basename
from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import (PetListView, PetDetailView, MilkListView, MilkDetailView,FarmView,
                    FodderListView, FodderDetailView, FarmDetailView, FarmListView)

routers = DefaultRouter()
routers.register(r"ferma", FarmView, basename="ferma-api")  #'farm/' va 'farm/<int:pk>' ning o'rniga 
urlpatterns = [
    # path('farm/', FarmListView.as_view()),
    # path('farm/<int:pk>/', FarmDetailView.as_view()),
    path('pet/', PetListView.as_view()),
    path('pet/<int:pk>/', PetDetailView.as_view()),
    path('milk/', MilkListView.as_view()),
    path('milk/<int:pk>/', MilkDetailView.as_view()),
    path('fodder/', FodderListView.as_view()),
    path('fodder/<int:pk>/', FodderDetailView.as_view()),
]


urlpatterns += routers.urls
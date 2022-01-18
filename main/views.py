from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAdminUser
from .permissions import IsAdminOrReadOnly
from .models import Pet, Milk, Fodder, Farm
from .serializers import PetSerializer, MilkSerializer, FodderSerializer, FarmSerializer


class FarmListView(ListCreateAPIView):
    permission_classes = (IsAdminUser,)
    queryset = Farm.objects.all()
    serializer_class = FarmSerializer


class FarmDetailView(RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAdminUser,)
    queryset = Farm.objects.all()
    serializer_class = FarmSerializer


class PetListView(ListCreateAPIView):
    permission_classes = (IsAdminUser,)
    queryset = Pet.objects.all()
    serializer_class = PetSerializer


class PetDetailView(RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAdminOrReadOnly,)
    queryset = Pet.objects.all()
    serializer_class = PetSerializer


class MilkListView(ListCreateAPIView):
    permission_classes = (IsAdminUser, )
    queryset = Milk.objects.all()
    serializer_class = MilkSerializer


class MilkDetailView(RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAdminOrReadOnly, )
    queryset = Milk.objects.all()
    serializer_class = MilkSerializer


class FodderListView(ListCreateAPIView):
    permission_classes = (IsAdminUser, )
    queryset = Fodder.objects.all()
    serializer_class = FodderSerializer


class FodderDetailView(RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAdminOrReadOnly, )
    queryset = Fodder.objects.all()
    serializer_class = FodderSerializer

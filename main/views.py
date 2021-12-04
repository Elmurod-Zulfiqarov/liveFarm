from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

from .permissions import IsAdminOrReadOnly
from .models import Pet, Milk, Fodder
from .serializers import PetSerializer, MilkSerializer, FodderSerializer


class PetListView(ListCreateAPIView):
    queryset = Pet.objects.all()
    serializer_class = PetSerializer


class PetDetailView(RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAdminOrReadOnly,)
    queryset = Pet.objects.all()
    serializer_class = PetSerializer


class MilkListView(ListCreateAPIView):
    queryset = Milk.objects.all()
    serializer_class = MilkSerializer


class MilkDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Milk.objects.all()
    serializer_class = MilkSerializer


class FodderListView(ListCreateAPIView):
    queryset = Fodder.objects.all()
    serializer_class = FodderSerializer


class FodderDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Fodder.objects.all()
    serializer_class = FodderSerializer

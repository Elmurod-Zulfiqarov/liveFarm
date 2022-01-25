from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAdminUser
from .permissions import IsAdminOrReadOnly
from .models import Pet, Milk, Fodder, Farm
from .serializers import PetSerializer, MilkSerializer, FodderSerializer, FarmSerializer
from rest_framework import viewsets
from rest_framework.parsers import JSONParser, MultiPartParser, FormParser

class FarmListView(ListCreateAPIView):
    permission_classes = (IsAdminUser,)
    queryset = Farm.objects.all()
    serializer_class = FarmSerializer


class FarmDetailView(RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAdminUser,)
    queryset = Farm.objects.all()
    serializer_class = FarmSerializer


# Bu klassni o'zi yuqoridagi 2 ta classni o'rnini bosadi.
class FarmView(viewsets.ModelViewSet):  
    permission_classes = (IsAdminOrReadOnly,)
    queryset = Farm.objects.all()
    serializer_class = FarmSerializer
    parser_classes = (JSONParser, MultiPartParser, FormParser,)

    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return super().delete(request, *args, **kwargs)

    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)


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

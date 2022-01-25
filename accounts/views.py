from rest_framework.viewsets import ModelViewSet
from rest_framework.parsers import JSONParser, MultiPartParser, FormParser
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .models import Accounts
from .serializers import AccountsSerializer


class AccountsViewSet(ModelViewSet):
    permission_classes = (IsAuthenticatedOrReadOnly,)
    parser_classes = (JSONParser, MultiPartParser, FormParser,)
    queryset = Accounts.objects.all()
    serializer_class = AccountsSerializer

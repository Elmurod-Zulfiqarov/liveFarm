from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAdminUser
from .models import Accounts
from .serializers import AccountsSerializer


class AccountsViewSet(ModelViewSet):
    permission_classes = (IsAdminUser,)
    queryset = Accounts.objects.all()
    serializer_class = AccountsSerializer




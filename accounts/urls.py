from django.urls import path, include
from rest_framework import routers

from .views import AccountsViewSet

router = routers.DefaultRouter()
router.register('accounts', AccountsViewSet)

urlpatterns = [
    path('', include(router.urls)),
]

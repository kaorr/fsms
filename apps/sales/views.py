from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from .models import Sale
from .serializers import SaleSerializer


class SaleViewSet(viewsets.ModelViewSet):
    queryset = Sale.objects
    serializer_class = SaleSerializer
    permission_classes = (IsAuthenticated,)

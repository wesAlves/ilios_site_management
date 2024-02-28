"""View for managing"""

from rest_framework import permissions, viewsets
from site_management.serializars import SiteSerializer
from .models import AvailableSite


# Create your views here.
class SiteManagementView(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited
    """

    queryset = AvailableSite.objects.all().order_by("-id")
    serializer_class = SiteSerializer
    permissions_classes = [permissions.IsAuthenticated]

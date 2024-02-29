"""View for managing"""

from rest_framework import permissions, viewsets
from site_management.serialiazers import (
    SiteSerializer,
    PageSerializer,
    SectionSerializer,
    ContainerSerializer,
    ThemeSerializer,
    TemplateSerializer,
)
from .models import AvailableSite, Page, Section, Container, Theme, Template


# Create your views here.
class SiteManagementView(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited
    """

    queryset = AvailableSite.objects.all().order_by("-id")
    serializer_class = SiteSerializer
    permissions_classes = [permissions.IsAuthenticated]


class PageViewSet(viewsets.ModelViewSet):
    queryset = Page.objects.all().order_by("-id")
    serializer_class = PageSerializer
    permissions_classes = [permissions.IsAuthenticated]


class SectionViewSet(viewsets.ModelViewSet):
    queryset = Section.objects.all().order_by("-id")
    serializer_class = SectionSerializer
    permissions_classes = [permissions.IsAuthenticated]


class ContainerViewSet(viewsets.ModelViewSet):
    queryset = Container.objects.all().order_by("-id")
    serializer_class = ContainerSerializer
    permissions_classes = [permissions.IsAuthenticated]


class ThemeViewSet(viewsets.ModelViewSet):
    queryset = Theme.objects.all().order_by("-id")
    serializer_class = ThemeSerializer
    permissions_classes = [permissions.IsAuthenticated]


class TemplateViewSet(viewsets.ModelViewSet):
    queryset = Template.objects.all().order_by("-id")
    serializer_class = TemplateSerializer
    permissions_classes = [permissions.IsAuthenticated]

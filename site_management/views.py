"""View for managing"""

from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import permissions, viewsets, generics

from site_management.serialiazers import (
    SiteSerializer,
    PageSerializer,
    SectionSerializer,
    ContainerSerializer,
    ThemeSerializer,
    TemplateSerializer,
)
from .models import AvailableSite, Page, Section, Container, Theme, Template

from rest_framework.filters import SearchFilter, OrderingFilter


# Create your views here.
class SiteManagementView(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited
    """

    filter_backends = [DjangoFilterBackend]

    queryset = AvailableSite.objects.all().order_by("-id")
    serializer_class = SiteSerializer
    permissions_classes = [permissions.IsAuthenticated]


class PageViewSet(viewsets.ModelViewSet):
    queryset = Page.objects.all().order_by("-id")
    serializer_class = PageSerializer
    permissions_classes = [permissions.IsAuthenticated]
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ["id", "name", "domain"]
    search_fields = ["=name", "id", "domain"]
    ordering_fields = ["name", "id"]
    ordering = ["id"]


class SectionViewSet(viewsets.ModelViewSet):

    filter_backends = [DjangoFilterBackend]

    queryset = Section.objects.all().order_by("-id")
    serializer_class = SectionSerializer
    permissions_classes = [permissions.IsAuthenticated]


class ContainerViewSet(viewsets.ModelViewSet):

    filter_backends = [DjangoFilterBackend]

    queryset = Container.objects.all().order_by("-id")
    serializer_class = ContainerSerializer
    permissions_classes = [permissions.IsAuthenticated]


class ThemeViewSet(viewsets.ModelViewSet):

    filter_backends = [DjangoFilterBackend]

    queryset = Theme.objects.all().order_by("-id")
    serializer_class = ThemeSerializer
    permissions_classes = [permissions.IsAuthenticated]


class TemplateViewSet(viewsets.ModelViewSet):

    filter_backends = [DjangoFilterBackend]

    queryset = Template.objects.all().order_by("-id")
    serializer_class = TemplateSerializer
    permissions_classes = [permissions.IsAuthenticated]

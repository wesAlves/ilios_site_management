"""View for managing"""

import json

from django.http import JsonResponse, HttpResponse
from django.views.generic import View
from django.core.serializers import serialize

from .models import AvailableSite, Page, Section, Container, Theme, Template


# Create your views here.
class SiteManagementView(View):
    """
    API endpoint that allows users to be viewed or edited
    """

    def get(self, request, id=None):

        if id != None:
            site = AvailableSite.objects.get(id=id)
            serialazed_site = serialize("json", [site])

            return JsonResponse(json.loads(serialazed_site), safe=False)

        sites = AvailableSite.objects.all()
        serialized_sites = serialize("json", sites)

        return JsonResponse(json.loads(serialized_sites), safe=False)


class PageView(View):
    def get(self, request, id=None):
        if id != None:
            try:
                page = Page.objects.get(id=id)
                serialazed_page = serialize("json", [page])

                return JsonResponse(json.loads(serialazed_page), safe=False)
            except:
                return JsonResponse({}, safe=False)

        try:
            pages = Page.objects.all()
            serialized_pages = serialize("json", pages)

            return JsonResponse(json.loads(serialized_pages), safe=False)
        except:
            return JsonResponse({}, safe=False)


#
class SectionView(View):
    def get(self, request, id=None):
        if id != None:
            section = Section.objects.get(id=id)
            serialazed_section = serialize("json", [section])

            return JsonResponse(json.loads(serialazed_section), safe=False)

        sections = Page.objects.all()
        serialized_sections = serialize("json", sections)

        return JsonResponse(json.loads(serialized_sections), safe=False)  #


#
class ContainerView(View):
    def get(self, request, id=None):
        if id != None:
            container = Section.objects.get(id=id)
            serialazed_container = serialize("json", [container])

            return JsonResponse(json.loads(serialazed_container), safe=False)

        containers = Page.objects.all()
        serialized_containers = serialize("json", containers)

        return JsonResponse(json.loads(serialized_containers), safe=False)


#
#
# class ThemeViewSet(viewsets.ModelViewSet):
#
#     filter_backends = [DjangoFilterBackend]
#
#     queryset = Theme.objects.all().order_by("-id")
#     serializer_class = ThemeSerializer
#     permissions_classes = [permissions.IsAuthenticated]
#
#
# class TemplateViewSet(viewsets.ModelViewSet):
#
#     filter_backends = [DjangoFilterBackend]
#
#     queryset = Template.objects.all().order_by("-id")
#     serializer_class = TemplateSerializer
#     permissions_classes = [permissions.IsAuthenticated]

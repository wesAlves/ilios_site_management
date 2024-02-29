"""View for managing"""

import json

import django.db.models
from django.http import JsonResponse, HttpResponse
from django.urls import reverse
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
            DetailOjectView(request, mode=Page, id=id)
            # site = AvailableSite.objects.get(id=id)
            # serialazed_site = serialize("json", [site])
            #
            # return JsonResponse(json.loads(serialazed_site), safe=False)

        sites = AvailableSite.objects.all()
        serialized_sites = serialize("json", sites)

        return JsonResponse(json.loads(serialized_sites), safe=False)


class PageView(View):
    def get(self, request, id=None):

        # filters = { "sections_page__id":5}
        # print(Page.objects.all().filter(sections_page__id=3))
        # print(filtered_object(Page, filters))

        if id != None:
            sections = getting_relate_object(Page, id, "sections_page")
            
            for section in sections:
                # getting_relate_object(Section, section.id, "")
                # print([content for content in section.children.all()])
                
                content = getting_relate_object(Section, section.id, 'children')
                # print(content)
                
                for c in content:
                    print(c.content)
            
            # print(sections)
            return JsonResponse(detail_oject(Page, id), safe=False)

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


def detail_oject(model, id):
    try:
        object = model.objects.get(id=id)
        serialazed_object = serialize("json", [object])

        return json.loads(serialazed_object)
    except:
        return {}


def filtered_object(model: django.db.models.Model, filters) -> django.db.models.Model:
    object = model.objects

    if len(filters) > 0:
        return object.filter(**filters)


def getting_relate_object(model: django.db.models.Model, id, related_name: str):
    object = model.objects.get(id=id)

    return object.__getattribute__(related_name).all()

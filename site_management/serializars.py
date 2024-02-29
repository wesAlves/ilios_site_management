"""rest framework serializers"""

from rest_framework import serializers

from .models import AvailableSite, Page, Section, Container, Theme, Template


class SiteSerializer(serializers.ModelSerializer):
    class Meta:
        model = AvailableSite
        fields = [
            "name",
            "domain",
            "atrributes",
            "theme",
            "author",
            "desctiption",
            "base_template",
        ]


class PageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Page
        fields = [
            "name",
            "keywords",
            "title",
            "body",
            "order",
            "templates",
            "domain"
        ]
        


class SectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Section
        fields = [
            "name",
            "order",
            "css_classes",
            "pages",
            "children",
            "aria",
        ]



class ContainerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Container
        fields = [
            "name",
            "type",
            "variant",
            "attribute",
            "content",
            "aria",
            "order",
            "css_classes",
        ]


class ThemeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Theme
        fields = ["name", "color", "logo", "graphisms"]


class TemplateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Template
        fields = ["name"]

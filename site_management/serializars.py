"""rest framework serializers"""

from rest_framework import serializers

from .models import AvailableSite, Page, Section, Container, Theme, Template


class SiteSerializer(serializers.HyperlinkedModelSerializer):
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


class PageSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Page
        fields = [
            "name",
            "site",
            "keyword",
            "title",
            "body",
            "order",
            "templates",
        ]


class SectionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        models = Section
        fields = [
            "name",
            "order",
            "css_class",
            "pages",
            "children",
            "aria",
        ]


class ContainerSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        models = Container
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


class ThemeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        models = Theme
        fields = ["name", "color", "logo", "graphisms"]


class TemplateSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        models = Template
        fields = ["name"]

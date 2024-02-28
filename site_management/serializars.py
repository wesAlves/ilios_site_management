"""rest framework serializers"""

from rest_framework import serializers

from .models import AvailableSite


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
    pass

class SectionSerializer(serializers.HyperlinkedModelSerializer):
    pass

class ContainerSerializer(serializers.HyperlinkedModelSerializer):
    pass

class ThemeSerializer(serializers.HyperlinkedModelSerializer):
    pass

class TemplateSerializer(serializers.HyperlinkedModelSerializer):
    pass
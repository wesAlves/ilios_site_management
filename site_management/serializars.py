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

from unittest.util import _MAX_LENGTH
from rest_framework_gis.serializers import GeoFeatureModelSerializer
from rest_framework import serializers

from .models import Boundary


class BoundarySerializer(GeoFeatureModelSerializer):
    area = serializers.CharField(max_length=100)

    class Meta:
        model = Boundary
        geo_field = "mpoly"
        fields = "__all__"

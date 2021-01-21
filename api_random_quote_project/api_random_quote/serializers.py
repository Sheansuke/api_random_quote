from api_random_quote_project.api_random_quote.models import Cita
from rest_framework import serializers


class CitaSerializers(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Cita
        fields = ["nombre","apellido","fecha"]
from api_random_quote_project.api_random_quote.models import Cita
from rest_framework import viewsets
from api_random_quote_project.api_random_quote.serializers import CitaSerializers
# Create your views here.
class CitaViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Cita.objects.all()
    serializer_class = CitaSerializers

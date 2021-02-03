from rest_framework import viewsets, permissions
from ems_api.models import EntranceExit
from ems_api.serializers import EntranceExitSerializer

# Create your views here.
class EntranceExitViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = EntranceExit.objects.all()
    serializer_class = EntranceExitSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
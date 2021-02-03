from rest_framework import viewsets, permissions
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response

from ems_api.models import EntranceExit
from ems_api.serializers import EntranceExitSerializer

# Create your views here.
class EntranceExitViewSet(viewsets.ViewSet):
    queryset = EntranceExit.objects.all()
    serializer_class = EntranceExitSerializer
    permission_classes = [permissions.IsAuthenticated]

    def list(self, request):
        queryset = EntranceExit.objects.order_by("-entrance_date")
        print(queryset)
        serializer = EntranceExitSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset = EntranceExit.objects.all()
        entrance_exit_obj = get_object_or_404(queryset, pk=pk)
        serializer = EntranceExitSerializer(entrance_exit_obj)
        return Response(serializer.data)

    def destroy(self, request, pk=None):
        obj = EntranceExit.objects.get(pk=pk)
        obj.delete()
        return Response(f"Delete: {obj}")

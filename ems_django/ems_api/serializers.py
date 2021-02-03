from rest_framework import serializers
from ems_api.models import EntranceExit


class EntranceExitSerializer(serializers.ModelSerializer):

    class Meta:
        model = EntranceExit
        fields = ("id", "user", "entrance_date", "exit_date")
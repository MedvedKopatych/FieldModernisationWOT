from rest_framework.serializers import ModelSerializer
from tanksbase.models import Tank


class TankSerializer(ModelSerializer):

    class Meta:
        model = Tank
        fields = '__all__'

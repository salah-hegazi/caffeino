from rest_framework_mongoengine.serializers import DocumentSerializer
from caffeino.listing.models import Pod, Machine


class PodSerializer(DocumentSerializer):
    class Meta:
        model = Pod
        fields = '__all__'


class MachineSerializer(DocumentSerializer):
    class Meta:
        model = Machine
        fields = '__all__'

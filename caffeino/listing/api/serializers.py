from rest_framework_mongoengine.serializers import DocumentSerializer
from caffeino.listing.models import Pod, Machine


class PodSerializer(DocumentSerializer):
    class Meta:
        model = Pod
        exclude = ('id', )

class MachineSerializer(DocumentSerializer):
    class Meta:
        model = Machine
        exclude = ('id', )

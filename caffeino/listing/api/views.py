from rest_framework.generics import ListAPIView

from .serializers import PodSerializer, MachineSerializer
from ..models import Pod, Machine

class PodListAPIView(ListAPIView):
    serializer_class = PodSerializer

    def get_queryset(self):
        queryset = Pod.objects.all()
        product_type = self.request.query_params.get('product_type', None)
        coffee_flavor = self.request.query_params.get('coffee_flavor', None)
        pack_size = self.request.query_params.get('pack_size', None)
        if product_type:
            queryset = queryset.filter(product_type=product_type)
        if coffee_flavor:
            queryset = queryset.filter(coffee_flavor=coffee_flavor)
        if pack_size:
            queryset = queryset.filter(pack_size=pack_size)
        return queryset


class MachineListAPIView(ListAPIView):
    serializer_class = MachineSerializer

    def get_queryset(self):
        queryset = Machine.objects.all()
        product_type = self.request.query_params.get('product_type', None)
        water_line_compatible = self.request.query_params.get(
            'water_line_compatible', None)
        if product_type:
            queryset = queryset.filter(product_type=product_type)
        if water_line_compatible:
            water_line_compatible_bool = (water_line_compatible == 'true')
            queryset = queryset.filter(
                water_line_compatible=water_line_compatible_bool)
        return queryset

from django.urls import path

from .views import PodListAPIView, MachineListAPIView


app_name = 'listings'
urlpatterns = [
    path('pods', view=PodListAPIView.as_view(), name='list-pods'),
    path('machines', view=MachineListAPIView.as_view(), name='list-machines'),
]
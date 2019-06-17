import random

from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.response import Response
from rest_framework import viewsets, status
from django.views.generic import View
from .models import XmlData,Device,AnaReport
from .serializers import AnaReportSerializer,DeviceSerializer,XmlReadSerializer
from rest_framework_mongoengine.viewsets import ModelViewSet
# from .filters import XmlReadFilter



class XmlReadViewSet(ModelViewSet):
    queryset = XmlData.objects.all()
    serializer_class = XmlReadSerializer
    my_filter_fields = ("anareport",)
    def get_kwargs_for_filtering(self):
        filtering_kwargs = {}
        for field in self.my_filter_fields:
            print(field)
            print(self.request.query_params)
            field_value = self.request.query_params.get(field)
            if field_value:
                filtering_kwargs[field] = field_value
        return filtering_kwargs

    def get_queryset(self):
        queryset = XmlData.objects.all()
        filtering_kwargs = self.get_kwargs_for_filtering()
        if filtering_kwargs:
            queryset = XmlData.objects.filter(**filtering_kwargs)
        return queryset

class AnaReportViewSet(viewsets.ModelViewSet):
    queryset = AnaReport.objects.all()
    serializer_class = AnaReportSerializer

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        XmlData.objects.filter(anareport = instance.id).delete()
        instance.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)



class DeviceViewSet(viewsets.ModelViewSet):
    queryset = Device.objects.all()
    serializer_class = DeviceSerializer


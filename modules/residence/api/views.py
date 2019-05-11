from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import generics, mixins, status
from .serializers import NewResidenceSerializers, ResidenceSerializers
from modules.residence.models import Residence

class ResidenceAPIView(mixins.CreateModelMixin, generics.ListAPIView):
    loockup_field = 'pk'
    serializer_class = NewResidenceSerializers

    def qet_queryset(self):
        qs = Residence.objects.all()
        return qs

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

class ResidenceListView(mixins.CreateModelMixin, generics.ListAPIView):
    loockup_field='pk'
    serializer_class = ResidenceSerializers

    def get_queryset(self):
        return Residence.objects.all()

class ResidenceRUDView(generics.RetrieveUpdateDestroyAPIView):
    loockup_field = 'pk'
    serializer_class = ResidenceSerializers
    def get_queryset(self):
        return Residence.objects.all()

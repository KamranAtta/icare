from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import generics, mixins, status
from .serializers import NewSchoolSerializers, SchoolSerializers
from modules.school.models import School

class SchoolAPIView(mixins.CreateModelMixin, generics.ListAPIView):
    loockup_field = 'pk'
    serializer_class = NewSchoolSerializers

    def qet_queryset(self):
        qs = School.objects.all()
        return qs

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

class SchoolListView(mixins.CreateModelMixin, generics.ListAPIView):
    loockup_field='pk'
    serializer_class = SchoolSerializers

    def get_queryset(self):
        return School.objects.all()

class SchoolRUDView(generics.RetrieveUpdateDestroyAPIView):
    loockup_field = 'pk'
    serializer_class = SchoolSerializers
    def get_queryset(self):
        return School.objects.all()

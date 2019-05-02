from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import generics, mixins, status
from .serializers import NewSchoolSerializers, SchoolSerializers
from modules.school.models import School

class SchoolAPIView(mixins.CreateModelMixin, generics.ListAPIView):
    loockup_field = 'pk'
    serializer = NewSchoolSerializers

    def qet_queryset(self):
        qs = School.objects.all()
        return qs

    def post(self, request, *args, **kwargs):
        serializer = NewSchoolSerializers(data=request.data)
        if not serializer.is_valid():
            return Response(serializer.error, status=status.HTTP_400_BAD_REQUEST)
        return self.create(request, *args, **kwargs)

class SchoolListView(mixins.CreateModelMixin, generics.ListAPIView):
    loockup_field='pk'
    serializer_class = SchoolSerializers

    def get_queryset(self):
        return School.objects.all()

class SchoolRUDView(generics.RetrieveUpdateDestroyAPIView):
    loockup_field = 'pk'
    serializer_class = SchoolSerializers
    def get_queryset(self, request):
        return School.objects.all()

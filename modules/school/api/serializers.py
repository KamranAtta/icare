from rest_framework import serializers
from modules.school.models import School


class SchoolSerializers(serializers.ModelSerializer):

    class Meta:
        model = School
        fields = '__all__'
        read_only_fields = ['id']


class NewSchoolSerializers(serializers.ModelSerializer):
    name = serializers.CharField(required=True)
    address = serializers.CharField(required=True)
    contact = serializers.CharField(required=True)
    city = serializers.CharField(required=True)
    country = serializers.CharField(required=True)

    class Meta:
        model = School
        fields = '__all__'
        read_only_fields = ['id']

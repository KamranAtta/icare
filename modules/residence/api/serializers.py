from rest_framework import serializers
from modules.residence.models import Residence


class ResidenceSerializers(serializers.ModelSerializer):

    class Meta:
        model = Residence
        fields = '__all__'
        read_only_fields = ['id']


class NewResidenceSerializers(serializers.ModelSerializer):
    name = serializers.CharField(required=True)
    address = serializers.CharField(required=True)
    contact = serializers.CharField(required=True)
    city = serializers.CharField(required=True)
    country = serializers.CharField(required=True)
    warden = serializers.CharField(required=True)

    class Meta:
        model = Residence
        fields = '__all__'
        read_only_fields = ['id']

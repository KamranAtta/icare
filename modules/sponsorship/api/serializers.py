from rest_framework import serializers
from modules.sponsorship.models import Sponsorship
from modules.sponsorship.api import helpers as sponsorship_helpers
from modules.expense.api import helpers as expense_helpers


class SponsorshipSerializers(serializers.ModelSerializer):

    class Meta:
        model = Sponsorship
        fields = '__all__'
        read_only_fields = ['id']


class NewSponsorshipSerializers(serializers.ModelSerializer):
    expense_id = serializers.UUIDField(required=True)
    user_id = serializers.UUIDField(required=True)
    donation = serializers.DecimalField(default=0.0, decimal_places=2, max_digits=10)
    duration = serializers.IntegerField(required=True)
    is_active = serializers.BooleanField(default=False)

    def create(self, validated_data, relation):
        expense = expense_helpers.get_by_id(self.validated_data['expense_id'])
        sponsorship = sponsorship_helpers.create_sponsorship(
            relation=relation,
            expense=expense,
            donation=self.validated_data.get('donation'),
            duration=self.validated_data['duration'],
            is_active=self.validated_data.get('is_active'),
        )
        return sponsorship



    class Meta:
        model = Sponsorship
        fields = '__all__'
        read_only_fields = ['id']

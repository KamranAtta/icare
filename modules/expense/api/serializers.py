from rest_framework import serializers
from modules.expense.models import Expense


class ExpenseSerializers(serializers.ModelSerializer):
    total_amount = serializers.SerializerMethodField()

    def get_total_amount(self, instance):
        return (instance.total_amount())

    class Meta:
        model = Expense
        fields = '__all__'
        read_only_fields = ['id']

class NewExpenseSerializer(serializers.ModelSerializer):
    school_id = serializers.UUIDField(required=True)
    # total_amount = serializers.SerializerMethodField()
    #
    # def get_total_amount(self, validated_data):
    #     return (self.validated_data.total_amount)

    class Meta:
        model = Expense
        fields = '__all__'
        read_only_fields= ['id']

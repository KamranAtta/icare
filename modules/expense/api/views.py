from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import generics, mixins, status
from modules.expense.models import Expense
from .serializers import ExpenseSerializers, NewExpenseSerializer
from modules.expense.api import helpers as expense_helpers


class ExpenseAPIView(mixins.CreateModelMixin, generics.ListAPIView):
    loockup_field = 'pk'
    serializer_class = NewExpenseSerializer

    def get_queryset(self):
        qs = Expense.objects.all()
        return qs

    def post(self, request, *args, **kwargs):
        serializer = NewExpenseSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return self.create(request, *args, **kwargs)

class ExpenseListView(generics.ListAPIView):
    loockup_field='pk'
    serializer_class= ExpenseSerializers

    def get_queryset(self):
        qs = Expense.objects.all()
        query = self.request.GET.get('school_id')
        if query is not None:
            qs = qs.filter(school_id=query)
        return qs


class ExpenseRUDView(generics.RetrieveUpdateDestroyAPIView):
    loockup_field='pk'
    serializer_class = ExpenseSerializers

    def get_queryset(self, request):
        return Expense.objects.filter(school_id=request.GET.get(school_id))

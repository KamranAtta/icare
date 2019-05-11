from django.shortcuts import render
from django.db.models import Q
from rest_framework.response import Response
from rest_framework import generics, mixins, viewsets, status
from rest_framework.decorators import detail_route, list_route
from .serializers import SponsorshipSerializers, NewSponsorshipSerializers
from modules.sponsorship.models import Sponsorship
from modules.users.api.student import helpers as student_helpers
from modules.expense.api import helpers as expense_helpers
from modules.users.api.guardian import helpers as guardian_helpers
from modules.sponsorship.api import helpers as sponsorship_helpers
from modules.users.api.user import helpers as user_helpers


class SponsorshipAPIView(mixins.CreateModelMixin, generics.ListAPIView):
    lookup_field = 'pk'
    serializer_class = NewSponsorshipSerializers

    def get_queryset(self):
        qs = Sponsorship.objects.all()
        query = self.request.Get.get('q')
        if query is not None:
            qs = qs.filter(Q(status__icontains=query))
        return qs

    def post(self, request, *args, **kwargs):
        # serializer = NewSponsorshipSerializers(data=request.data)
        # if not serializer.is_valid():
        #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        #
        # student = (student_helpers.get_student_by_user_id(request.data['user_id']))
        # if not student:
        #     return Response({'error': 'Student doesnot exist'}, status=status.HTTP_400_BAD_REQUEST)
        #
        # guardian = guardian_helpers.get_guardian_by_user_id(self.request.user.id)
        # if not guardian:
        #     return Response({'error': 'Guardian doesnot exist'}, status=status.HTTP_400_BAD_REQUEST)
        #
        # relation = user_helpers.create_relation(guardian, student)
        # if not relation:
        #     return Response({'error': 'Can not process request'}, status=status.HTTP_400_BAD_REQUEST)

        return self.create(request, *args, **kwargs)


class SponsorshipAPI(viewsets.ViewSet):
    @list_route(methods=['POST'], url_path='set_sponsorship')
    def set_sponsorship(self, request):
        serializer = NewSponsorshipSerializers(data=request.data)
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        student = (student_helpers.get_student_by_user_id(request.data['user_id']))
        if not student:
            return Response({'error': 'Student doesnot exist'}, status=status.HTTP_400_BAD_REQUEST)

        guardian = guardian_helpers.get_guardian_by_user_id(self.request.user.id)
        if not guardian:
            return Response({'error': 'Guardian doesnot exist'}, status=status.HTTP_400_BAD_REQUEST)

        relation = user_helpers.create_relation(guardian, student)
        if not relation:
            return Response({'error': 'Can not process request'}, status=status.HTTP_400_BAD_REQUEST)

        expense = expense_helpers.get_by_id(request.data['expense_id'])
        if not expense:
            return Response({'error': 'Expense doesnot exist'}, status=status.HTTP_400_BAD_REQUEST)

        sponsorship = serializer.create(serializer.validated_data, relation)

        response = {
            'id': sponsorship.pk,
            'expense': str(sponsorship.expense.id),
            'relation': str(sponsorship.relation.id),
            'donation': sponsorship.donation,
            'duration': sponsorship.duration,
            'is_active': sponsorship.is_active,
        }
        return Response(response, status=status.HTTP_201_CREATED)

class SponsorshipListView(mixins.CreateModelMixin, generics.ListAPIView):
    loockup_field='pk'
    serializer_class = SponsorshipSerializers

    def get_queryset(self):
        return Sponsorship.objects.all()

class SponsorshipRUDView(generics.RetrieveUpdateDestroyAPIView):
    loockup_field = 'pk'
    serializer_class = SponsorshipSerializers
    def get_queryset(self):
        return Sponsorship.objects.all()

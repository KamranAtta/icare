from django.contrib import admin
from django.urls import path
import uuid
from rest_framework import routers
from .views import SponsorshipAPI, SponsorshipAPIView, SponsorshipRUDView, SponsorshipListView

app_name = 'sponsorship'
router = routers.SimpleRouter()

router.register('', SponsorshipAPI, base_name='set_sponsorship')

urlpatterns = tuple(router.urls)
urlpatterns += (
    path('', SponsorshipListView.as_view(), name = 'sponsorship-list'),
    path('create', SponsorshipAPIView.as_view(), name = 'sponsorship-create'),
    path('<uuid:pk>', SponsorshipRUDView.as_view(), name='sponsorship-rud'),
)

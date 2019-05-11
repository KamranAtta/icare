from .views import ResidenceAPIView, ResidenceListView, ResidenceRUDView
from django.contrib import admin
from django.urls import path
import uuid
from rest_framework import routers

app_name = 'residence'
router = routers.SimpleRouter()
# router.register('create', SchoolAPIView, 'schools')

urlpatterns = tuple(router.urls)
urlpatterns+=(
    path('', ResidenceListView.as_view(), name='residence-list'),
    path('create', ResidenceAPIView.as_view(), name='residence-create'),
    path('<uuid:pk>', ResidenceRUDView.as_view(), name= 'residence-rud'),
)

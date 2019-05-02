from .views import SchoolAPIView, SchoolListView, SchoolRUDView
from django.contrib import admin
from django.urls import path
import uuid
from rest_framework import routers

app_name = 'school'
router = routers.SimpleRouter()
# router.register('create', SchoolAPIView, 'schools')

urlpatterns = tuple(router.urls)
urlpatterns+=(
    path('', SchoolListView.as_view, name='school-list'),
    path('create', SchoolAPIView.as_view, name='school-created'),
    path('<uuid:pk>', SchoolRUDView.as_view, name= 'school-rud')
)

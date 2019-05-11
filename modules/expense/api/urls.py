from django.urls import path
from django.contrib import admin
from .views import ExpenseAPIView, ExpenseListView, ExpenseRUDView
import uuid
from rest_framework import routers

app_name = 'expense'
router = routers.SimpleRouter()

urlpatterns = tuple(router.urls)
urlpatterns+=(
    path('', ExpenseListView.as_view(), name='expense-list'),
    path('create', ExpenseAPIView.as_view(), name='expense-create'),
    path('<uuid:pk>', ExpenseRUDView.as_view(),name='expense-rud'),
)

from django.urls import path
from .views import StaffBaseViewSet

urlpatterns = [
    path('staff/', StaffBaseViewSet.as_view(), name='staff-list'),
]
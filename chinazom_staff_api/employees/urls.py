from django.urls import path
from .views import StaffRoleView

urlpatterns = [
    path('staff/', StaffRoleView.as_view(), name='staff-list'),
]
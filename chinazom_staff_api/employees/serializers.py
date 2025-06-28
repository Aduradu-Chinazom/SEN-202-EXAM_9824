from rest_framework import serializers
from .models import StaffBase, Manager, Intern

class StaffBaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = StaffBase
        fields = '__all__'

        def get_role(self, specific_role):
            if specific_role == 'Manager':
                return 'Manager'
            elif specific_role == 'Intern':
                return 'Intern'
            else:
                return 'Staff'

class ManagerSerializer(serializers.ModelSerializer):
    staffBase = StaffBaseSerializer()

    class Meta:
        model = Manager
        fields = '__all__'

        @overide
        def get_role(self, specific_role):
            if specific_role == 'Manager':
                return 'Manager'
            elif specific_role == 'Intern':
                return 'Intern'
            else:
                return 'Staff'

class InternSerializer(serializers.ModelSerializer):
    staffBase = StaffBaseSerializer()
    mentor = ManagerSerializer()

    class Meta:
        model = Intern
        fields = '__all__'

        @overide
        def get_role(self, specific_role):
            if specific_role == 'Manager':
                return 'Manager'
            elif specific_role == 'Intern':
                return 'Intern'
            else:
                return 'Staff'

    
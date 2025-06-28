from rest_framework import serializers
from .models import StaffBase, Manager, Intern

class StaffBaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = StaffBase
        fields = '__all__'

        def get_role(self, obj):
            return obj.get_role_label()

class ManagerSerializer(serializers.ModelSerializer):
    staffBase = StaffBaseSerializer()

    class Meta:
        model = Manager
        fields = '__all__'

    

class InternSerializer(serializers.ModelSerializer):
    staffBase = StaffBaseSerializer()
    mentor = ManagerSerializer()

    class Meta:
        model = Intern
        fields = '__all__'

   
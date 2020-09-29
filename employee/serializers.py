from .models import Employee, Accessory
from rest_framework.serializers import ModelSerializer

class EmployeeSerializer(ModelSerializer):
    class Meta:
        model = Employee
        fields = ['url', 'id', 'name', 'surname', 'img']


class AccessorySerializer(ModelSerializer):
    class Meta:
        model = Accessory
        fields = ['url', 'id', 'owner', 'name', 'prise', 'comment', 'img']
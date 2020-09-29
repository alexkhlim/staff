from django import forms
from employee.models import Employee, Accessory


class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = ('name', 'surname', 'img')

class AccessoryForm(forms.ModelForm):
    class Meta:
        model = Accessory
        fields = ('name', 'prise', 'comment', 'owner', 'img')
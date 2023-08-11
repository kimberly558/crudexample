from django import forms
from employee.models import Employee


class EmployeeForm(forms.ModelForm):
    model = Employee
    fields = "__all__"


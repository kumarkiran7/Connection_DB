from django import forms
from .models import *

class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee_Details
        fields = ['Emp_Id','Name','Email','First_Name','Last_Name','Father_Name','Mother_Name',
                  'Dob','Blood_Group','Contact_Number','Emergency_Number','Present_Address','Permanent_Address','Qualification' ]
    
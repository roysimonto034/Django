from django import forms
from . models import Employee
class EmployeeForm(forms.Form):

	  empname = forms.CharField(widget=forms.TextInput,max_length=100,label='myname')
	  email = forms.EmailField(widget=forms.TextInput,label='email address')
	  Indian = forms.CharField(widget=forms.CheckboxInput,max_length=100)
	  message = forms.CharField(widget=forms.Textarea)

class Empmodel(forms.ModelForm):

	 class Meta:
	 	   model = Employee
	 	   fields = "__all__"
from django import forms
from . models import Item,Worker

class FormName(forms.Form): #important
    name=forms.CharField()
    email=forms.EmailField()
    text=forms.CharField(widget=forms.Textarea)

    def clean_name(self):
        name=self.cleaned_data['name']
        if len(name)<5:
            raise forms.ValidatioError("got it")
        return name

class UserName(forms.ModelForm): #important
      class Meta:
          model=Item
          fields = '__all__'

class Workername(forms.ModelForm):
      def clean_salary(self):
          ipsal=self.cleaned_data['salary']
          if ipsal<50000:
             raise forms.ValidationError('Minimum sal shld be more than this')
          return ipsal

      class Meta:
          model=Worker
          fields='__all__'
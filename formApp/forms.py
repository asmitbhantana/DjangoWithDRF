from django import forms
from .models import FormsModel


class MyForms(forms.Form):
    name = forms.CharField(max_length=20)

    def clean_name(self):
        print("I am from form", self.cleaned_data)
        name = self.cleaned_data['name']
        # clean here, that gets saved in the database
        return name.lower()


class FormsModelForm(forms.ModelForm):
    class Meta:
        model = FormsModel
        fields = ['name', 'email']

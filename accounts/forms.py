from django import forms

from django.contrib.auth import get_user_model

User = get_user_model()

class LoginForm(forms.Form):
    username = forms.CharField(max_length=150)
    password = forms.CharField(max_length=128, widget=forms.PasswordInput())


class RegisterForm(forms.Form):
    first_name = forms.CharField(max_length=30)
    last_name = forms.CharField(max_length=150)
    username = forms.CharField(max_length=150)
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput())
    confirm_password = forms.CharField(widget=forms.PasswordInput())

    def clean_email(self):
        if User.objects.filter(email=self.cleaned_data['email']).exists():
            raise forms.ValidationError('This email is already Register!')
        return self.cleaned_data['email']

    def clean_username(self):
        if User.objects.filter(username=self.cleaned_data['username']).exists():
            raise forms.ValidationError('This username is already taken!')
        return self.cleaned_data['username']

    def clean(self):
        if self.cleaned_data['password'] != self.cleaned_data['confirm_password']:
            raise forms.ValidationError('Passwords doesn\'t matches!')



    # class Meta:
        # model = User
        # fields = ['first_name', 'last_name', 'username', 'email', 'password', ]

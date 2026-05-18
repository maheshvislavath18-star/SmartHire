from django import forms
from django.contrib.auth.models import User

class RegisterForm(forms.ModelForm):

    password = forms.CharField(widget=forms.PasswordInput)
    user_type = forms.ChoiceField(choices=[
        ('recruiter', 'Recruiter'),
        ('applicant', 'Applicant')
    ])

    class Meta:
        model = User
        fields = ['username', 'password']
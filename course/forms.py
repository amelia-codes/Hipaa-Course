from django.forms import ModelForm
from course.models import *
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class MyUserCreationForm(UserCreationForm):
    #authentication
    email = forms.EmailField()
    firstname = forms.CharField()
    lastname = forms.CharField()
    class Meta:
        model = User
        fields = {'firstname','lastname','username','email','password'} #make so that must have valid 3T email to take the test (for now)?


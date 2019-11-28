from django import forms
from .models import Complain
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.forms import DateInput

class ComplainForm(forms.ModelForm):
    
    class Meta:
        model=Complain
        fields=('phone','claim')
        labels = {
            'phone': ('핸드폰번호'),
            'claim':('건의사항'),    
        }
        


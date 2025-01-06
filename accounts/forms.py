from .models import Account
from django import forms
from django.contrib import messages
class RegistrationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder':'Password',
    
    }))
    confirm_password = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder':'Confrim Password',
       
    }))


    class Meta:
        model=Account
        fields=['first_name','last_name','phone_number','email','password']


    def __init__(self, *args, **kwargs):
            super(RegistrationForm,self).__init__(*args, **kwargs)
            self.fields['first_name'].widget.attrs['placeholder']='First Name'
            self.fields['last_name'].widget.attrs['placeholder']='Last Name'
            self.fields['phone_number'].widget.attrs['placeholder']='Phone Number'
            self.fields['email'].widget.attrs['placeholder']='Email'
            for field in self.fields:
                self.fields[field].widget.attrs['class']='form-control'
                self.fields[field].widget.attrs['required']=True
                
             
   
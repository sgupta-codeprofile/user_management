from django import forms
from django.core.validators import ValidationError

class DateInput(forms.DateInput):
    input_type = 'date'

class SignupForm(forms.Form):
    inputCity=[
        ('Noida','Noida'),
        ('Delhi','Delhi'),
        ('Faridabad','Faridabad'),
        ('Bangalore','Bangalore')
    ]
    firstName=forms.CharField(max_length=50,required=True,widget=forms.TextInput(attrs={'placeholder':'First Name',
                                                                          'class':'form-control',
                                                                          'id': "firstName"
                                                                          }))
    lastName=forms.CharField(max_length=50,required=True,widget=forms.TextInput(attrs={'placeholder':'Last Name',
                                                                          'class':'form-control',
                                                                          'id': "lastName"
                                                                          }))
    username=forms.CharField(max_length=50,required=True,widget=forms.TextInput(attrs={'placeholder':'Username',
                                                                          'class':'form-control',
                                                                          'id': "username"
                                                                          }))
    userEmail=forms.EmailField(required=True,widget=forms.EmailInput(attrs={'placeholder':'Email',
                                                              'class': 'form-control',
                                                              'id': "email"
                                                              }))
    password=forms.CharField(required=True,widget=forms.PasswordInput(attrs={'class':'form-control','id':'password','placeholder':'Password'}))
    confirmPassword=forms.CharField(required=True,widget=forms.PasswordInput(attrs={'class':'form-control','id':'confirmPassword','placeholder':'Password'}))
    dateOfBirth= forms.DateField(label='What is your birth date?',required=True,widget=DateInput)
    phoneNumber=forms.CharField(max_length=12,required=True,widget=forms.NumberInput(attrs={'placeholder':'Phone Number',
                                                                          'class':'form-control',
                                                                          'id': "phoneNumber"
                                                                          }))
    # selectCity=forms.ChoiceField(label="Select City",widget=forms.Select(choices=inputCity,attrs={'class':'form-control'}))
    chooseGender=forms.ChoiceField(required=True,widget=forms.RadioSelect(attrs={}),choices=[('1','Male'),('2','Female')])

    def clean(self):
        cleaned_data = self.cleaned_data
        keys=list(cleaned_data.keys())
        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("confirmPassword")
        if password != confirm_password:
            print("not match")
            raise ValidationError(
                "password and confirm_password does not match",params={'val':keys[4]}
            )
        return "not match"


class LoginForm(forms.Form):
    userName=forms.CharField(max_length=50,required=True,widget=forms.TextInput(attrs={
        'class':'form-control',
        'autocomplete':'off',
        'placeholder':'Username'
    }))
    password=forms.CharField(max_length=50,required=True,widget=forms.PasswordInput(attrs={
        'class': 'form-control',
        'autocomplete': 'off',
        'placeholder': 'Password'
    }))

class uploadImageUser(forms.Form):
    image=forms.ImageField()




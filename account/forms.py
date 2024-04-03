from django import forms
from .models import User, Address
from django.core.exceptions import ValidationError
from django.core import validators
from django.contrib.auth.forms import ReadOnlyPasswordHashField


# custom form validation
# def start_with_0(value):
#     if value[0] != '0':
#         raise forms.ValidationError("Phone should start with 0")


class LoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))  # validators=[start_with_0, validators.MaxLengthValidator(11)]
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))

    def clean_phone(self):
        username = self.cleaned_data.get('username')
        if len(username) > 80:
            raise ValidationError('تلفن وارد شده معتبر نیست', code='invalid_phone')

        return username


class AddressCreationForm(forms.ModelForm):
    user = forms.IntegerField(required=False)
    fullname = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Amirali Amiri'}))
    email = forms.EmailField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'example@email.com'}))
    phone = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': '09123456789'}))
    address = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': '123 street'}))
    postal_code = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': '123'}))

    class Meta:
        model = Address
        fields = '__all__'


class OtpLoginForm(forms.Form):
    phone = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}), validators=[validators.MaxLengthValidator(11)])


class CheckOtpForm(forms.Form):
    code = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}), validators=[validators.MaxLengthValidator(4)])
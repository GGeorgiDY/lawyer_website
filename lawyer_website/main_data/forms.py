from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, PasswordChangeForm
from .models import CustomUser


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ['email', 'first_name', 'last_name', 'password1', 'password2']
        labels = {
            'email': 'Email',
            'first_name': 'First Name',
            'last_name': 'Last Name',
            'password1': 'Password',
            'password2': 'Confirm Password',
        }
        help_texts = {
            'first_name': 'This field is optional.',
            'last_name': 'This field is optional.',
        }


class CustomAuthenticationForm(AuthenticationForm):
    class Meta:
        model = CustomUser
        fields = ['email', 'password']


class CustomPasswordChangeForm(PasswordChangeForm):
    class Meta:
        model = CustomUser


class ProfileForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ['email', 'first_name', 'last_name']


# class ContactForm(forms.Form):
#     name = forms.CharField(max_length=100, required=True, widget=forms.TextInput(attrs={
#         'class': 'form-control',
#         'placeholder': 'Your Name'
#     }))
#     email = forms.EmailField(required=True, widget=forms.EmailInput(attrs={
#         'class': 'form-control',
#         'placeholder': 'Your Email'
#     }))
#     phone = forms.CharField(max_length=15, required=True, widget=forms.TextInput(attrs={
#         'class': 'form-control',
#         'placeholder': 'Your Phone Number'
#     }))
#     message = forms.CharField(widget=forms.Textarea(attrs={
#         'class': 'form-control',
#         'rows': 5,
#         'placeholder': 'Your Message'
#     }), required=True)


class CustomForm(forms.Form):
    header = forms.CharField(max_length=200, required=True, widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Enter header'
    }))
    text = forms.CharField(widget=forms.Textarea(attrs={
        'class': 'form-control',
        'rows': 5,
        'placeholder': 'Enter text'
    }), required=True)


from django import forms
from .models import Client


class ContactForm(forms.Form):
    message_name = forms.CharField(max_length=100,
                                   widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'name'}))
    message_email = forms.EmailField(max_length=100,
                                     widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'email'}))
    message = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'message'}))


class ClientForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = ['first_name', 'last_name', 'email', 'phone', 'resume', 'status']
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'phone': forms.TextInput(attrs={'class': 'form-control'}),
            'resume': forms.Textarea(attrs={'class': 'form-control', 'rows': 5}),
            'status': forms.Select(attrs={'class': 'form-control'}),
        }
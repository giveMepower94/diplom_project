from django import forms


class ContactForm(forms.Form):
    message_name = forms.CharField(max_length=100,
                                   widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'name'}))
    message_email = forms.EmailField(max_length=100,
                                     widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'email'}))
    message = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'message'}))



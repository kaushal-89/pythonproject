from django import forms
class ContactForm(forms.Form):
    yourname = forms.CharField(max_length=100, label="Name")
    email = forms.EmailField(required=False, label="Email-id")
    subject = forms.CharField(max_length=100)
    message = forms.CharField(widget=forms.Textarea)
from django import forms


class ContactForm(forms.Form):
    name = forms.CharField(max_length=200)
    email = forms.EmailField(max_length=250)
    subject = forms.CharField(max_length=200)
    message = forms.CharField(max_length=2000, widget=forms.Textarea())


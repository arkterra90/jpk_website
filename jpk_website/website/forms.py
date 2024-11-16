from django import forms
from .models import Subscriber  # Adjust the import based on your app structure

class SubscriberForm(forms.ModelForm):
    class Meta:
        model = Subscriber
        exclude = ['dateSub']  # Exclude the dateSub field
        labels = {
            'nameFirst': 'First Name',
            'nameLast': 'Last Name',
            'subEmail': 'Email Address',
        }

class EmailForm(forms.Form):
    subject = forms.CharField(max_length=255, required=True, label="Email Subject")
    message = forms.CharField(widget=forms.Textarea, required=True, label="Email Message")
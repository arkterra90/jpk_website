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

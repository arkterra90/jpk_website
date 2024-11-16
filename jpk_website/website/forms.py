from django import forms
from .models import Subscriber  # Import the Subscriber model

# Form for subscribing to a newsletter or updates
class SubscriberForm(forms.ModelForm):
    """
    A form for collecting subscriber details, excluding the subscription date.
    """

    class Meta:
        model = Subscriber  # Use the Subscriber model
        exclude = ['dateSub']  # Exclude the dateSub field as it defaults to the current date
        labels = {
            'nameFirst': 'First Name',  # Customize the label for the nameFirst field
            'nameLast': 'Last Name',  # Customize the label for the nameLast field
            'subEmail': 'Email Address',  # Customize the label for the subEmail field
        }

# Form for sending an email to multiple recipients
class EmailForm(forms.Form):
    """
    A simple form for composing an email with a subject and message.
    """
    subject = forms.CharField(
        max_length=255,
        required=True,
        label="Email Subject",  # Label for the subject field
    )
    message = forms.CharField(
        widget=forms.Textarea,  # Use a textarea widget for multi-line input
        required=True,
        label="Email Message",  # Label for the message field
    )

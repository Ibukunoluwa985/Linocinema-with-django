from django import forms

# contact us form
class ContactUsForm(forms.Form):
    name = forms.CharField(max_length=50)
    email = forms.EmailField(max_length=250)
    subject = forms.CharField(max_length=100)
    message = forms.CharField(max_length=500)

    def __init__(self, *args, **kwargs):
        super(ContactUsForm, self).__init__(*args, **kwargs)
        self.fields['name'].widget = forms.TextInput(attrs={'placeholder': 'your name',})
        self.fields['email'].widget = forms.EmailInput(attrs={'placeholder': 'your email',})
        self.fields['subject'].widget = forms.TextInput(attrs={'placeholder': 'subject',})
        self.fields['message'].widget = forms.Textarea(attrs={'placeholder': 'message'})
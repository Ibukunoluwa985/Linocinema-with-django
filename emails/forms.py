from django import forms

class ReachoutForm(forms.Form):
    subject = forms.CharField(max_length=250)
    message = forms.CharField(max_length=5000)
    def __init__(self, *args, **kwargs):
        super(ReachoutForm, self).__init__(*args, **kwargs)
        self.fields['subject'].widget = forms.TextInput(attrs={'placeholder': 'Subject'})
        self.fields['message'].widget = forms.Textarea(attrs={'row': 4, 'col': 40})
        self.fields['subject'].label = False
        self.fields['message'].label = False

class PersonalReachoutForm(forms.Form):
    email = forms.EmailField(max_length=250)
    request_name = forms.CharField(max_length=250)
    request_link = forms.URLField(max_length=250)

    def __init__(self, *args, **kwargs):
        super(PersonalReachoutForm, self).__init__(*args, **kwargs)
        self.fields['email'].widget = forms.EmailInput(attrs={'placeholder': 'Email'})
        self.fields['request_name'].widget = forms.TextInput(attrs={'placeholder': 'Request Name'})
        self.fields['request_link'].widget = forms.URLInput(attrs={'placeholder': 'Request Link'})
        self.fields['email'].label = False
        self.fields['request_name'].label = False
        self.fields['request_link'].label = False

class PersonalFailReachoutForm(forms.Form):
    email = forms.EmailField(max_length=250)
    request_name = forms.CharField(max_length=250)

    def __init__(self, *args, **kwargs):
        super(PersonalFailReachoutForm, self).__init__(*args, **kwargs)
        self.fields['email'].widget = forms.EmailInput(attrs={'placeholder': 'Email'})
        self.fields['request_name'].widget = forms.TextInput(attrs={'placeholder': 'Request Name'})
        self.fields['email'].label = False
        self.fields['request_name'].label = False
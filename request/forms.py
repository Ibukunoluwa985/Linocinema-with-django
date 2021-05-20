from django import forms
from .forms import *

class MovieRequestForm(forms.Form):
    movie_name = forms.CharField(max_length=500)
    movie_year = forms.IntegerField()
    questionnaire_name = forms.CharField(max_length=50)
    email = forms.EmailField(max_length=250)

    def __init__(self, *args, **kwargs):
        super(MovieRequestForm, self).__init__(*args, **kwargs)
        self.fields['movie_name'].widget = forms.TextInput(attrs={'placeholder': 'Movie name'})
        self.fields['movie_name'].label = False
        self.fields['movie_year'].widget = forms.NumberInput(attrs={'placeholder': 'Movie year'})
        self.fields['movie_year'].label = False
        self.fields['email'].widget = forms.EmailInput(attrs={'placeholder': 'your email (required)'})
        self.fields['email'].label = False
        self.fields['questionnaire_name'].widget = forms.TextInput(attrs={'placeholder': 'Your name (optional)'})
        self.fields['questionnaire_name'].label = False

class TvshowRequestForm(forms.Form):
    tvshow_name = forms.CharField(max_length=500)
    tvshow_season = forms.CharField(max_length=500)
    tvshow_year = forms.IntegerField()
    questionnaire_name = forms.CharField(max_length=50)
    email = forms.EmailField(max_length=250)

    def __init__(self, *args, **kwargs):
        super(TvshowRequestForm, self).__init__(*args, **kwargs)
        self.fields['tvshow_name'].widget = forms.TextInput(attrs={'placeholder': 'Tvshow name'})
        self.fields['tvshow_name'].label = False
        self.fields['tvshow_season'].widget = forms.TextInput(attrs={'placeholder': 'Tvshow season'})
        self.fields['tvshow_season'].label = False
        self.fields['tvshow_year'].widget = forms.NumberInput(attrs={'placeholder': 'Tvshow year'})
        self.fields['tvshow_year'].label = False
        self.fields['email'].widget = forms.EmailInput(attrs={'placeholder': 'your email (required)'})
        self.fields['email'].label = False
        self.fields['questionnaire_name'].widget = forms.TextInput(attrs={'placeholder': 'Your name (optional)'})
        self.fields['questionnaire_name'].label = False
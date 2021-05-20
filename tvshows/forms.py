from django import forms
from tvshows.models import Tvshows, Season

class TvshowUploadForm(forms.ModelForm):
    class Meta:
        model = Tvshows
        exclude = ('user', 'image', 'added_on')
    def __init__(self, *args, **kwargs):
        super(TvshowUploadForm, self).__init__(*args, **kwargs)
        self.fields['image_link'].widget = forms.TextInput(attrs={'placeholder': 'image link'})
        self.fields['title'].widget = forms.TextInput(attrs={'placeholder': 'title'})
        self.fields['language'].widget = forms.TextInput(attrs={'placeholder': 'language'})
        self.fields['rate'].widget = forms.TextInput(attrs={'placeholder': 'rate'})
        self.fields['trailer'].widget = forms.TextInput(attrs={'placeholder': 'trailer'})
        self.fields['genre'].widget = forms.TextInput(attrs={'placeholder': 'genre'})
        self.fields['year'].widget = forms.NumberInput(attrs={'placeholder': 'year'})
        self.fields['description'].widget = forms.Textarea(attrs={'placeholder': 'description(plot)'})

class TvshowSeasonForm(forms.ModelForm):
    class Meta:
        model = Season
        exclude = ('added_on',)
    def __init__(self, *args, **kwargs):
        super(TvshowSeasonForm, self).__init__(*args, **kwargs)
        self.fields['season_number'].widget = forms.NumberInput(attrs={'placeholder': 'season number'})
        self.fields['episode_number'].widget = forms.NumberInput(attrs={'placeholder': 'episode number'})
        self.fields['episode_download_link'].widget = forms.TextInput(attrs={'placeholder': 'episode download link'})
from django import forms
from movies.models import Movies

class MovieUploadForm(forms.ModelForm):
    class Meta:
        model = Movies
        exclude = ('user', 'permission', 'image', 'added_on')
    def __init__(self, *args, **kwargs):
        super(MovieUploadForm, self).__init__(*args, **kwargs)
        self.fields['image_link'].widget = forms.TextInput(attrs={'placeholder': 'image link'})
        self.fields['title'].widget = forms.TextInput(attrs={'placeholder': 'title'})
        self.fields['language'].widget = forms.TextInput(attrs={'placeholder': 'language'})
        self.fields['rate'].widget = forms.TextInput(attrs={'placeholder': 'rate'})
        self.fields['trailer'].widget = forms.TextInput(attrs={'placeholder': 'trailer'})
        self.fields['genre'].widget = forms.TextInput(attrs={'placeholder': 'genre'})
        self.fields['year'].widget = forms.NumberInput(attrs={'placeholder': 'year'})
        self.fields['link'].widget = forms.TextInput(attrs={'placeholder': 'download link'})
        self.fields['mb'].widget = forms.NumberInput(attrs={'placeholder': 'size in mb'})
        self.fields['director'].widget = forms.TextInput(attrs={'placeholder': 'director'})
        self.fields['director_link'].widget = forms.TextInput(attrs={'placeholder': 'director link'})
        self.fields['subtitle'].widget = forms.TextInput(attrs={'placeholder': 'subtitle'})
        self.fields['description'].widget = forms.Textarea(attrs={'placeholder': 'description(plot)'})
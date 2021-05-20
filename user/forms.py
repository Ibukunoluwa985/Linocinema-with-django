from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User

class RegisterForm(UserCreationForm):
    username = forms.CharField(max_length=250, required='required', widget=forms.TextInput(attrs={'placeholder': 'choose username',}))
    email = forms.EmailField(max_length=250, required='required', widget=forms.EmailInput(attrs={'placeholder': 'active email address',}))
    password1 = forms.CharField(max_length=250, required='required', widget=forms.PasswordInput(attrs={'placeholder': 'choose password',}))
    password2 = forms.CharField(max_length=250, required='required', widget=forms.PasswordInput(attrs={'placeholder': 'confirm password',}))

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2' )

class LoginForm(AuthenticationForm):
    username = forms.CharField(max_length=250, widget=forms.TextInput(attrs={'placeholder': 'your username',}))
    password = forms.CharField(max_length=250, widget=forms.PasswordInput(attrs={'placeholder': 'your password',}))
    
    class Meta:
        model = User
        fields = ('username', 'password' )
    def __init__(self, *args, **kwargs):
        super(LoginForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget = forms.TextInput(attrs={'placeholder': 'your username',})
        self.fields['username'].label = False
        self.fields['password'].widget = forms.PasswordInput(attrs={'placeholder': 'your password',})
        self.fields['password'].label = False

class UpdateFirstNameForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('first_name',)
    def __init__(self, *args, **kwargs):
        super(UpdateFirstNameForm, self).__init__(*args, **kwargs)
        self.fields['first_name'].widget = forms.TextInput(attrs={'placeholder': 'first name',})
        self.fields['first_name'].label = False

class UpdateLastNameForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('last_name',)
    def __init__(self, *args, **kwargs):
        super(UpdateLastNameForm, self).__init__(*args, **kwargs)
        self.fields['last_name'].widget = forms.TextInput(attrs={'placeholder': 'last name',})
        self.fields['last_name'].label = False

class DisactivateAccountForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('is_active',)
    def __init__(self, *args, **kwargs):
        super(DisactivateAccountForm, self).__init__(*args, **kwargs)
        self.fields['is_active'].widget = forms.TextInput(attrs={'type': 'hidden',})
        self.fields['is_active'].label = False

class ReactivateAccountForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('email', )
    def __init__(self, *args, **kwargs):
        super(ReactivateAccountForm, self).__init__(*args, **kwargs)
        self.fields['email'].widget = forms.EmailInput(attrs={'placeholder': 'your email'})
        self.fields['email'].label = False
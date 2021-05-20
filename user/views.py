from .forms import (LoginForm, RegisterForm, ReactivateAccountForm, DisactivateAccountForm, UpdateFirstNameForm, UpdateLastNameForm)
from django.shortcuts import render, redirect, HttpResponseRedirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import (View, TemplateView)
from django.contrib.auth.models import User
from django.contrib import messages

def login_redirect(request):
    return redirect('user_login')
def logout_redirect(request):
    return redirect('user_logout')
def home_redirect(request):
    return redirect('landing_page')

class UserInfoPage(LoginRequiredMixin, TemplateView):
    template_name = "user/user_info_page.html"
    login_url = 'user_login'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['update_first_name_form'] = UpdateFirstNameForm()
        context['update_last_name_form'] = UpdateLastNameForm()
        context['disactivate_user_form'] = DisactivateAccountForm()
        return context

class Login(View):
    template_name = 'user/login_page.html'
    context = {}

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            messages.info(request, 'You are logged in already!')
            return redirect('landing_page')
        else:
            self.context['login_form'] = LoginForm()
            return render(request, self.template_name, self.context)

    def post(self, request, *args, **kwargs):
        username = request.POST['username']
        password = request.POST['password']
        authenticate_user = authenticate(username=username, password=password)

        if authenticate_user is not None:
            if authenticate_user.is_active:
                login(request, authenticate_user)
                messages.success(request, f'Welcome { request.user.username }!')
                return redirect('user_info_page')
            else:
                messages.info(request, 'Inactive user!')
                return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
        else:
            messages.error(request, "Check user's credentail!")
            return redirect('user_login')

class Register(View):
    template_name = 'user/register_page.html'
    context = {}

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            messages.info(request, 'You are logged in already!')
            return redirect('landing_page')
        else:
            self.context['register_form'] = RegisterForm()
            return render(request, self.template_name, self.context)

    def post(self, request, *args, **kwargs):
        register_form = RegisterForm(request.POST)
        if register_form.is_valid():
            username = register_form.cleaned_data.get('username')
            email = register_form.cleaned_data.get('email')
            raw_password = register_form.cleaned_data.get('password1')
            if User.objects.filter(username=username).exists():
                messages.error(request, "Username already exists. Try another")
                return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
            elif User.objects.filter(email=email).exists():
                messages.error(request, "Email already exists. Try another")
                return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
            else:
                register_form.save()
                user = authenticate(username=username, email=email, password=raw_password)
                login(request, user)
                messages.success(request, f'Welcome "{ request.user.username }"')
                return redirect('user_info_page')
        return render(request, self.template_name, {'register_form': register_form})

class Logout(LoginRequiredMixin, View):
    login_url = 'user_login'
    
    def get(self, request):
        logout(request)
        messages.success(request, 'You are now logged out!')
        return redirect('landing_page')    

class ReactivateUser(View):
    template_name = "user/reactivate_user_page.html"
    context = {}

    def get(self, request, *args, **kwargs):
        self.context['reactivate_user_form'] = ReactivateAccountForm()
        return render(request, self.template_name, self.context)

    def post(self, request, *args, **kwargs):
        form = ReactivateAccountForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data.get('email')
            if User.objects.filter(email=email).exists():
                activate_user = User.objects.get(email=email)
                if activate_user.is_active == False:
                    activate_user.is_active = True
                    activate_user.save()
                    messages.success(request, "User reactivated")
                    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
                else:
                    messages.info(request, "User already activated")
                    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
            else:
                messages.error(request, "User does not exists")
                return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
        else:
            messages.error(request, "Something went wrong! Check email.")
            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

class DisactivateUser(LoginRequiredMixin, View):
    template_name = "user/user_info_page.html"
    login_url = 'user_login'
    context = {}

    def get(self, request, *args, **kwargs):
        self.context['disactivate_user_form'] = DisactivateAccountForm()
        return render(request, self.template_name, self.context)

    def post(self, request, *args, **kwargs):
        form = DisactivateAccountForm(request.POST)
        if form.is_valid():
            disactivate_user = User.objects.get(username=request.user)
            disactivate_user.is_active = False
            disactivate_user.save()
            messages.success(request, "User disactivated")
            return redirect('landing_page')

class DeleteUser(LoginRequiredMixin, View):
    template_name = "user/user_info_page.html"
    login_url = 'user_login'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)

    def post(self, request, *args, **kwargs):
        form = DisactivateAccountForm(request.POST)
        if form.is_valid() and not request.user.is_superuser or not request.user.is_staff:
            user_delete = User.objects.get(username=request.user)
            user_delete.delete()
            messages.success(request, "User deleted")
            return redirect('landing_page')

class UpdateFirstName(LoginRequiredMixin, View):
    template_name = "user/user_info_page.html"
    login_url = 'user_login'
    context = {}

    def get(self, request, *args, **kwargs):
        self.context['update_first_name_form'] = UpdateFirstNameForm()
        return render(request, self.template_name, self.context)

    def post(self, request, *args, **kwargs):
        form = UpdateFirstNameForm(request.POST)
        if form.is_valid():
            change_first_name = form.cleaned_data.get('first_name')
            first_name = User.objects.get(username=request.user)
            first_name.first_name = change_first_name
            first_name.save()
            messages.success(request, "First name Updated!")
            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

class UpdateLastName(LoginRequiredMixin, View):
    template_name = "user/user_info_page.html"
    login_url = 'user_login'
    context = {}

    def get(self, request, *args, **kwargs):
        self.context['update_last_name_form'] = UpdateLastNameForm()
        return render(request, self.template_name, self.context)

    def post(self, request, *args, **kwargs):
        form = UpdateLastNameForm(request.POST)
        if form.is_valid():
            change_last_name = form.cleaned_data.get('last_name')
            last_name = User.objects.get(username=request.user)
            last_name.last_name = change_last_name
            last_name.save()
            messages.success(request, "Last name Updated!")
            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
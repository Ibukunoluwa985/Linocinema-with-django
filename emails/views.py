from .forms import ReachoutForm, PersonalReachoutForm, PersonalFailReachoutForm
from django.shortcuts import render, redirect, HttpResponseRedirect
from django.core.mail import send_mail, BadHeaderError
from django.views.generic import TemplateView, View
from LinoCinema.settings import EMAIL_HOST_USER
from django.contrib.auth.models import User
from email.errors import HeaderParseError
from django.contrib import messages
from django.template import loader
import socket

class Emails(TemplateView):
    template_name = "emails/email_page.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['reachout_form'] = ReachoutForm()
        context['personal_reachout_form'] = PersonalReachoutForm()
        context['personal_reachout_fail_form'] = PersonalFailReachoutForm()
        return context

class Reachout(View):
    def get(self, request, *args, **kwargs):
        return redirect('emails_page')

    def post(self, request, *args, **kwargs):
        form = ReachoutForm(request.POST)
        if form.is_valid():
            context = {}
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']
            from_email = EMAIL_HOST_USER
            context['name'] =  request.user.username
            context['subject'] = subject
            context['message'] = message
            to_email = User.objects.filter(is_active=True).values_list('email', flat=True)
            actual_message = loader.render_to_string('emails/templates/reachout_email.html', context)

            try:
                send_mail(subject, actual_message, from_email, [to_email], fail_silently = False, html_message=actual_message)
                messages.success(request, 'Email sent')
                return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
            except socket.gaierror:
                messages.error(request, 'No internet connect')
                return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
            except HeaderParseError:
                messages.error(request, 'A user has an invalid domain')
                return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
            except BadHeaderError:
                messages.error(request, 'Bad header')
                return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
            except TimeoutError:
                messages.error(request, 'Time out')
                return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
            except ValueError as e:
                messages.error(request, f'{e}')
                return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    
class PersonalReachout(View):
    def get(self, request, *args, **kwargs):
        return redirect('emails_page')

    def post(self, request, *args, **kwargs):
        form = PersonalReachoutForm(request.POST)
        if form.is_valid():
            context = {}
            subject = 'Available Now'
            request_name = form.cleaned_data['request_name']
            request_link = form.cleaned_data['request_link']
            from_email = EMAIL_HOST_USER
            to_email = form.cleaned_data['email']
            context['to_email'] = to_email
            context['name'] =  request.user.username
            context['subject'] = subject
            context['request_name'] = request_name
            context['request_link'] = request_link
            actual_message = loader.render_to_string('emails/templates/request_success_email.html', context)

            try:
                send_mail(subject, actual_message, from_email, [to_email], fail_silently = False, html_message=actual_message)
                messages.success(request, 'Email sent')
                return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
            except socket.gaierror:
                messages.error(request, 'No internet connect')
                return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
            except HeaderParseError:
                messages.error(request, 'A user has an invalid domain')
                return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
            except BadHeaderError:
                messages.error(request, 'Bad header')
                return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
            except TimeoutError:
                messages.error(request, 'Time out')
                return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    
class PersonalFailReachout(View):
    def get(self, request, *args, **kwargs):
        return redirect('emails_page')

    def post(self, request, *args, **kwargs):
        form = PersonalFailReachoutForm(request.POST)
        if form.is_valid():
            context = {}
            subject = 'Not Available'
            request_name = form.cleaned_data['request_name']
            from_email = EMAIL_HOST_USER
            to_email = form.cleaned_data['email']

            context['to_email'] = to_email
            context['name'] =  request.user.username
            context['subject'] = subject
            context['request_name'] = request_name
            actual_message = loader.render_to_string('emails/templates/request_fail_email.html', context)

            try:
                send_mail(subject, actual_message, from_email, [to_email], fail_silently = False, html_message=actual_message)
                messages.success(request, 'Email sent')
                return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
            except socket.gaierror:
                messages.error(request, 'No internet connect')
                return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
            except HeaderParseError:
                messages.error(request, 'A user has an invalid domain')
                return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
            except BadHeaderError:
                messages.error(request, 'Bad header')
                return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
            except TimeoutError:
                messages.error(request, 'Time out')
                return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    
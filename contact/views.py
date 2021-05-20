from django.shortcuts import render, HttpResponseRedirect
from django.core.mail import send_mail, BadHeaderError
from LinoCinema.settings import EMAIL_HOST_USER
from email.errors import HeaderParseError
from django.views.generic import View
from django.contrib import messages
from django.template import loader
from .forms import ContactUsForm
import socket

class ContactPage(View):
    template_name='contact/contact_page.html'
    def get(self, request, *args, **kwargs):
        context = {}
        context['contact_us_form'] = ContactUsForm()
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        form = ContactUsForm(request.POST)
        if form.is_valid():
            context = {}
            name = form.cleaned_data.get('name')
            email = form.cleaned_data.get('email')
            subject = form.cleaned_data.get('subject')
            message = form.cleaned_data.get('message')
            context['name'] = name
            context['email'] = email
            context['subject'] = subject
            context['message'] = message
            actual_message = loader.render_to_string('emails/templates/contact_email.html', context)

            try:
                send_mail(subject, actual_message, email, [EMAIL_HOST_USER], fail_silently = False, html_message=actual_message)
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
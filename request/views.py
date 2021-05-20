from django.shortcuts import render, HttpResponseRedirect
from django.core.mail import send_mail, BadHeaderError
from .forms import MovieRequestForm, TvshowRequestForm
from django.views.generic import (View, TemplateView)
from LinoCinema.settings import EMAIL_HOST_USER
from email.errors import HeaderParseError
from django.shortcuts import redirect
from django.views.generic import View
from django.contrib import messages
from django.template import loader
import socket

class RequestPage(TemplateView):
    template_name='request/request_page.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['movie_request_form'] = MovieRequestForm()
        context['tvshow_request_form'] = TvshowRequestForm()
        return context

class MovieRequest(View):
    def get(self, request, *args, **kwargs):
        return redirect('request_page')

    def post(self, request, *args, **kwargs):
        form = MovieRequestForm(request.POST)
        if form.is_valid():
            context = {}
            movie_name = request.POST.get('movie_name')
            movie_year = request.POST.get('movie_year')
            name = request.POST.get('questionnaire_name')
            subject = 'Movie Request'
            email_from = request.POST.get('email')
            context['movie_name'] = movie_name
            context['movie_year'] = movie_year
            context['name'] = name
            context['subject'] = subject
            context['email_from'] = email_from
            actual_message = loader.render_to_string('emails/templates/movie_request_email.html', context)

            try:
                send_mail(subject, actual_message, email_from, [EMAIL_HOST_USER], fail_silently = False, html_message=actual_message)
                messages.success(request, 'Movie request sent!')
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

class TvshowRequest(View):
    def get(self, request, *args, **kwargs):
        return redirect('request_page')

    def post(self, request, *args, **kwargs):
        form = TvshowRequestForm(request.POST)
        if form.is_valid():
            context = {}
            tvshow_name = request.POST.get('tvshow_name')
            tvshow_season = request.POST.get('tvshow_season')
            tvshow_year = request.POST.get('tvshow_year')
            name = request.POST.get('questionnaire_name')
            subject = 'Tvshow Request'
            email_from = request.POST.get('email')
            context['tvshow_name'] = tvshow_name
            context['tvshow_season'] = tvshow_season
            context['tvshow_year'] = tvshow_year
            context['name'] = name
            context['subject'] = subject
            context['email_from'] = email_from
            actual_message = loader.render_to_string('emails/templates/tvshow_request_email.html', context)

            try:
                send_mail(subject, actual_message, email_from, [EMAIL_HOST_USER], fail_silently = False, html_message=actual_message)
                messages.success(request, 'Tvshow request sent!')
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

from django.views.generic import TemplateView, CreateView
from .forms import ReviewForm
from django.views.generic.edit import CreateView
from .models import DjServices, Reviews
from django.shortcuts import render
from django.http import HttpResponseBadRequest
import os
from django.urls import reverse_lazy
from django.views.generic import TemplateView, DetailView
from django.views import View
from django.http import JsonResponse

# Create your views here.
class DjPageView(TemplateView):
    template_name = 'dj/dj_index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # context['contact_form'] = ContactForm()
        context['services'] = DjServices.objects.all()
        return context


class DjReviewView(CreateView):
    form_class = ReviewForm
    template_name = 'dj/dj_reviews_page.html'
    success_url = reverse_lazy('this-justin')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['review_form'] = ReviewForm()
        context['review'] = Reviews.objects.all()
        context['services'] = DjServices.objects.all()

        return context


class ReviewPost(View):
    def post(self, request):
        review_form = ReviewForm(request.POST)

        if review_form.is_valid():
            try:
                review_form.save()
                print('Email sent successfully!')
                print('Data saved successfully!')
                return JsonResponse({'success': True})  # Return success JSON response
            except Exception as e:
                error_message = f'An error occurred while sending email or saving data: {str(e)}'
                print(error_message)
                return JsonResponse({'success': False, 'error_message': error_message})

            else:
                form_errors = contact_form.errors.as_json()
                return JsonResponse({'success': False, 'form_errors': form_errors})

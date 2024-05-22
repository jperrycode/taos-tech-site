
from django.views.generic import TemplateView

from .models import DjServices


# Create your views here.
class DjPageView(TemplateView):
    template_name = 'dj/dj_index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # context['contact_form'] = ContactForm()
        context['services'] = DjServices.objects.all()
        return context


class DjReviewView(TemplateView):
    template_name = 'dj/dj_reviews_page.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # context['contact_form'] = ContactForm()
        context['review'] = Reviews.objects.all()
        return context
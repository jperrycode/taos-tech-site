from django.shortcuts import render, redirect
from django.shortcuts import HttpResponse
from .forms import ContactForm
from django.core.mail import send_mail, BadHeaderError
from main.settings import DEFAULT_FROM_EMAIL as df_email
from django.views import View
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from django.views.generic import TemplateView
from django.urls import reverse



# Create your views here.


# class ContactUsView(View):
#     def post(self, request):
#         contact_form = ContactForm(request.POST or None)

#         if contact_form.is_valid():
#             contact_form.save()


#             # subject = contact_form.cleaned_data['customer_contact_subject']

#             # body = {
#             #     'name': contact_form.cleaned_data['customer_name'],
#             #     'message': contact_form.cleaned_data['customer_notes'],     

#             # }

#             # message = "\n".join(body.values())
#             # print(message)
#             # try:
#             #     send_mail(subject, message, df_email, ['taos.haus.tech@gmail.com'])
#             # except BadHeaderError:
#             #     return redirect('contact_fail')  # Redirect to fail page if there's an error

#             return HttpResponse(request, SuccessPageView)

#         print(contact_form.errors)
#         return render(request, 'frontend/contact_fail.html',)  # Redirect to fail page if form is invalid


class Contact_model_view(CreateView):
    form_class = ContactForm
    template_name = 'frontend/index_form.html'
    success_url = reverse_lazy('contact_suc')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['contact_form'] = ContactForm()
        return context


# home page view with contact modelform context
class MainPageView(View):
    def get(self, request):
        contact_form = ContactForm()
        context = {'contact_form': contact_form}
        return render(request, 'frontend/index.html', context)


class EcomPageView(View):
    def get(self, request):
        contact_form = ContactForm()
        context = {'contact_form': contact_form}
        return render(request, 'frontend/index_ecom.html', context)


class WebPageView(View):
    def get(self, request):
        contact_form = ContactForm()
        context = {'contact_form': contact_form}
        return render(request, 'frontend/index_web.html', context)


def SuccessPageView(request):
    return render(request, 'frontend/index_success.html')


class FailPageView(View):
    template_name = 'frontend/contact_fail.html'


class TeamPageView(View):
    def get(self, request):
        contact_form = ContactForm()
        context = {'contact_form': contact_form}
        return render(request, 'frontend/index_team.html', context)


class StagePageView(View):
    def get(self, request):
        contact_form = ContactForm()
        context = {'contact_form': contact_form}
        return render(request, 'frontend/stageing.html', context)





# class DjPageView(TemplateView):
#     template_name = 'dj/dj_index.html'
#
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['contact_form'] = ContactForm()
#         context['services'] = DjServices.objects.all()
#         return context

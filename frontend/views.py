from django.shortcuts import render, redirect
from django.shortcuts import HttpResponse
from .forms import ContactForm
from django.core.mail import send_mail, BadHeaderError
from main.settings import DEFAULT_FROM_EMAIL as df_email
from django.views import View
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt
import requests


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


class HardwarePageView(View):
    def get(self, request):
        contact_form = ContactForm()
        context = {'contact_form': contact_form}
        return render(request, 'frontend/index_hardware.html', context)


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


class CreateCustomerChannelView(View):
    @csrf_exempt
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def post(self, request):
        # Extract customer information from the request
        customer_name = request.POST.get('customer_name')
        customer_email = request.POST.get('customer_email')
        customer_message = request.POST.get('customer_message')

        # Connect to Discord and create a new channel
        webhook_url = 'YOUR_DISCORD_WEBHOOK_URL_HERE'
        new_channel_response = requests.post(webhook_url, json={'name': customer_name})

        if new_channel_response.status_code == 200:
            # Channel created successfully, extract channel ID
            channel_id = new_channel_response.json().get('id')

            # Send message to the newly created channel
            message_data = {
                'content': f'New customer: {customer_name}\nEmail: {customer_email}\nMessage: {customer_message}'
            }
            send_message_response = requests.post(f'https://discord.com/api/channels/{channel_id}/messages',
                                                  json=message_data)

            if send_message_response.status_code == 200:
                return JsonResponse({'success': True})
            else:
                return JsonResponse({'success': False, 'error': 'Failed to send message to Discord channel'})
        else:
            return JsonResponse({'success': False, 'error': 'Failed to create Discord channel'})

    # Implement the chat widget separately based on your preferred technology, such as WebSocket for real-time communication.

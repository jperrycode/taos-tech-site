from django.shortcuts import render, redirect
from django.shortcuts import HttpResponse
from .forms import ContactForm
from django.core.mail import send_mail, BadHeaderError
from main.settings import DEFAULT_FROM_EMAIL




from_email = DEFAULT_FROM_EMAIL
# Create your views here.

# send email functionality and save customer form data to model

def contact_us(request):
  if request.method == 'POST':
    contact_form = ContactForm(request.POST or None)
    if contact_form.is_valid():
      contact_form.save()
      subject = contact_form.cleaned_data['customer_contact_subject'] 
      user_email=contact_form.cleaned_data['customer_email']
      body = {            
			'name': contact_form.cleaned_data['customer_name'],   
			'message': contact_form.cleaned_data['customer_notes'], 
			}
      
      message = "\n".join(body.values())
      print(message)
      try:
        send_mail(subject, message, from_email, [user_email]) 
        
      except BadHeaderError:
        return HttpResponse('Invalid header found.')
      
    contact_form = ContactForm()
  print(contact_form.errors)
  return redirect('home')
  


# home page view with contact modelform context
def mainpageview(request):
    contact_form = ContactForm()
    context = {'contact_form': contact_form,}
    return render(request, 'index.html', context)

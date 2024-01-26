from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.template import loader
from django.core.mail import send_mail
from .forms import ContactForm
from django.template.loader import render_to_string
from django.utils.html import strip_tags

def home(request):
  template = loader.get_template('home.html')
  return HttpResponse(template.render())

def about(request):
  template = loader.get_template('about.html')
  return HttpResponse(template.render())

def services(request):
  template = loader.get_template('services.html')
  return HttpResponse(template.render())


def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            name = strip_tags(form.cleaned_data['name'])
            message = render_to_string('email_template.html', {'name': form.cleaned_data['name'], 'email': form.cleaned_data['email'], 'subject': form.cleaned_data['subject']})
            from_email = form.cleaned_data['email']
            to_email = 'onlinestorez700@gmail.com'  # Muutke see vastavalt oma vajadustele
            send_mail(name, message, from_email, [to_email], html_message=message)
            return render(request, 'email_send_success.html')

    else:
        form = ContactForm()

    return render(request, 'contact.html', {'form': form})

    return render(request, 'contact.html', {'form': form})

def clients(request):
  template = loader.get_template('clients.html')
  return HttpResponse(template.render())

def gallery(request):
  template = loader.get_template('gallery.html')
  return HttpResponse(template.render())
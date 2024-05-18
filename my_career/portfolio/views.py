from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.template.loader import render_to_string

from .forms import ContactForm, ClientForm


def index(request):
    return render(request, 'portfolio/index.html')


def about(request):
    return render(request, 'portfolio/about.html')


def resume(request):
    return render(request, 'portfolio/resume.html')


def service(request):
    return render(request, 'portfolio/service.html')


def project(request):
    return render(request, 'portfolio/project.html')


def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            message_name = form.cleaned_data['message_name']
            message_email = form.cleaned_data['message_email']
            message = form.cleaned_data['message']

            html_view = render_to_string('portfolio/email.html', {
                'message_name': message_name,
                'message_email': message_email,
                'message': message
            })

            send_mail('Заявка пользователя', 'here message', 'noreply@yandex.ru', ['bigsosiska98@gmail.com'], html_message=html_view)

            return redirect('index')
    else:
        form = ContactForm()

    return render(request, 'portfolio/contact.html', {'form': form})


def create_client(request):
    if request.method == 'POST':
        form = ClientForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = ClientForm()
    return render(request, 'portfolio/create_client.html', {'form': form})
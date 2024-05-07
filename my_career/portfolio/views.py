from django.shortcuts import render


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
    return render(request, 'portfolio/contact.html')

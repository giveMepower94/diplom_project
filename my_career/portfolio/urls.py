from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about_page'),
    path('resume/', views.resume, name='resume'),
    path('services/', views.service, name='service'),
    path('project/', views.project, name='project'),
    path('contact/', views.contact, name='contact'),
    path('create_client/', views.create_client, name='create_client'),
]
from django.urls import path
from . import views

urlpatterns = [
    path('contact/', views.contact, name = 'contact'), 
    path('faqs', views.view_faqs, name='view_faqs'),
]
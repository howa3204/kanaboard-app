from django.urls import path

from . import views

app_name = 'landing'
urlpatterns = [
    path('', views.home, name='home'),
    path('about', views.about, name='about'),
    path('privacy', views.privacy, name='privacy'),
    path('terms', views.terms, name='terms'),
    path('refund', views.refund, name='refund'),
]

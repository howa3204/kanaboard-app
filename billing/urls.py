from django.urls import path

from . import views

app_name = 'billing'
urlpatterns = [
    path('billing/', views.billing, name='billing'),
    path('webhook/', views.stripe_webhook),
]

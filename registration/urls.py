from django.urls import path

from . import views

app_name = 'registration'
urlpatterns = [
    path('register/', views.register_page, name='register'),
    path('activate/<uidb64>/<token>', views.Verification.as_view(), name='activate')
]

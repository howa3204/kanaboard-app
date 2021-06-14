from django.urls import path

from . import views

app_name = 'authentication'
urlpatterns = [
    path('login/', views.login_page, name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('update_billing/', views.update_billing, name='update_billing'),
]

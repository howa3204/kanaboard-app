from django.urls import path

from . import views

app_name = 'account_settings'
urlpatterns = [
    path('account/', views.account, name='account'),
    path('delete_account/', views.delete_account, name='delete_account'),
    path('password_change/', views.MyPasswordChangeView.as_view(), name='password_change'),
    path('password_change_done/', views.MyPasswordResetDoneView.as_view(), name='password_change_done'),
]

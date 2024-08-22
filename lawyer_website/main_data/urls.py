from django.contrib.auth.views import LogoutView
from django.urls import path
from lawyer_website.main_data.views import about, home, register, user_login, change_password, profile_view, location
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('', home, name='home'),
    path('about/', about, name='about'),
    path('register/', register, name='register'),
    path('login/', user_login, name='login'),
    path('logout/', LogoutView.as_view(next_page='home'), name='logout'),
    path('change-password/', change_password, name='change_password'),

    path('password-reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),
    path('password-reset/done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),

    path('profile/', profile_view, name='profile'),
    path('location/', location, name='location'),
]


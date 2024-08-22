from django.contrib.auth.views import LogoutView
from django.urls import path
from lawyer_website.main_data.views import about, home, register, user_login, change_password

urlpatterns = [
    path('', home, name='home'),
    path('about/', about, name='about'),
    path('register/', register, name='register'),
    path('login/', user_login, name='login'),
    path('logout/', LogoutView.as_view(next_page='home'), name='logout'),
    path('change-password/', change_password, name='change_password'),
]


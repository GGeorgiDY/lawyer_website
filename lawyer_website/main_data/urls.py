from django.urls import path
from lawyer_website.main_data.views import about, home

urlpatterns = [
    path('', home, name='home'),
    path('about/', about, name='about'),
]

from django.urls import path
from lawyer_website.services.views import service_detail, service_list

urlpatterns = [
    path('', service_list, name='service_list'),
    path('<int:pk>/', service_detail, name='service_detail'),
]


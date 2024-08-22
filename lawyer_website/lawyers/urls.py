from django.urls import path
from lawyer_website.lawyers.views import lawyer_list, lawyer_detail

urlpatterns = [
    path('', lawyer_list, name='lawyer_list'),
    path('<int:pk>/', lawyer_detail, name='lawyer_detail'),
]


from django.contrib import admin
from django.urls import path, include
from lawyer_website import main_data

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', include("lawyer_website.main_data.urls")),
    path('lawyers/', include("lawyer_website.lawyers.urls")),
    path('news/', include("lawyer_website.news.urls")),
    path('services/', include("lawyer_website.services.urls")),
]

from django.contrib import admin
from .models import Lawyer


@admin.register(Lawyer)
class LawyerAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'position', 'email')
    search_fields = ('first_name', 'last_name', 'position', 'email')
    list_filter = ('position',)




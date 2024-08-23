from django.contrib import admin
from .models import Service


# @admin.register(Service)
# class ServiceAdmin(admin.ModelAdmin):
#     list_display = ('name',)
#     search_fields = ('name',)


@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

    fieldsets = (
        (None, {
            'fields': ('name',)
        }),
        ('Details', {
            'fields': ('description',)
        }),
    )



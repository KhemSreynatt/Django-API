from django.contrib import admin
from .models import Profile


class Filter(admin.ModelAdmin):
    list_display=('id','email','created_at','role','is_active',)
    list_filter=('is_active','role','created_at',)

admin.site.register(Profile, Filter)
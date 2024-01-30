from django.contrib import admin
from . import models

@admin.register(models.Post)
class AuthorAdmin(admin.ModelAdmin):
    list_display=('titel','id','status','slug','author')
    prepopulated_fields ={'slug':('titel',),}

admin.site.register(models.Category)


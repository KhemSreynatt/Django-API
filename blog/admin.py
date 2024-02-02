from django.contrib import admin
from . import models

@admin.register(models.Post)
class AuthorAdmin(admin.ModelAdmin):
    login_template='blog/login.html'
    list_display=('title','id','status','slug','author')
    prepopulated_fields ={'slug':('title',),}
    site_header="Admin Template"
    

admin.site.register(models.Category)


from django.contrib import admin

class AdminTemplates(admin.AdminSite):
    site_header ="Admin Template",

admin_site= AdminTemplates(name='AdminTemplate')


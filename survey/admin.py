from django.contrib import admin
from survey.models import autum
# Register your models here.

class ContactAdmin(admin.ModelAdmin):
    list_display = ('name','branch', 'worker','market','time')

admin.site.register(autum,ContactAdmin)
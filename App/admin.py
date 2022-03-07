from http import client
from django.contrib import admin
from App.models import Client
# Register your models here.
class ClientAdmin(admin.ModelAdmin):
    list_display =['name','phone','email','gender','created_at']
    search_fields =['name','phone','email','gender']
    list_per_page =8

admin.site.register(Client,ClientAdmin)


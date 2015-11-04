from django.contrib import admin
from client.models import client_info,client_balance,client_pd,market

# Register your models here.
admin.site.register(client_balance)
admin.site.register(client_pd)
admin.site.register(client_info)
admin.site.register(market)
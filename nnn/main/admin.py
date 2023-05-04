from django.contrib import admin
from .models import uslug, Gorod, Cruise, Booking
from django.contrib.admin import AdminSite

AdminSite.site_header = "Онлайн покупка билетов"
admin.site.register(uslug)
admin.site.register(Gorod)
admin.site.register(Cruise)
admin.site.register(Booking)

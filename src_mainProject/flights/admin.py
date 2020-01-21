from django.contrib import admin
from .models import Airport, Flight
# Register your models here.

admin.site.register(Airport)
admin.site.register(Flight)

# Estamos registrando nuestros 'models'
# con el admin.site  -  Así, admin.site
# será capaz de manipular Airports 
# and Flights

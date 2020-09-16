from django.contrib import admin

from .models import CoffeeMachine, CoffeePod

admin.site.register(CoffeeMachine)
admin.site.register(CoffeePod)

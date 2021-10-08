from django.contrib import admin

# Register your models here.
from .models import vehicle, driver, assaign_and_unassaign, order


admin.site.register(vehicle)
admin.site.register(driver)
admin.site.register(assaign_and_unassaign)
admin.site.register(order)



from django.contrib import admin

# Register your models here.
from .models import *

admin.site.register(DonationPlace)
admin.site.register(DonationCamp)
admin.site.register(BloodBank)
admin.site.register(BloodUnit)
admin.site.register(BloodRequest)
admin.site.register(User)
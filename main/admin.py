from django.contrib import admin
from .models import SmartBin, Pickup, WasteReport, Feedback,UserProfile

# Register your models here.

admin.site.register(SmartBin)
admin.site.register(Pickup)
admin.site.register(WasteReport)
admin.site.register(Feedback)
admin.site.register(UserProfile)


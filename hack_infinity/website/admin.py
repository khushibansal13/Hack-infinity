from django.contrib import admin
from .models import Invitation,Invitation_confirmation,CreateEventInfo
# Register your models here.
admin.site.register(Invitation)
admin.site.register(Invitation_confirmation)
admin.site.register(CreateEventInfo)

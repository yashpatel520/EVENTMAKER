from django.contrib import admin
from .models import EventRegistration,FeedBack
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User,Group


class EventRegistrationAdmin(admin.ModelAdmin):
    pass
admin.site.register(EventRegistration, EventRegistrationAdmin)

class FeedBackAdmin(admin.ModelAdmin):
    pass
admin.site.register(FeedBack, FeedBackAdmin)

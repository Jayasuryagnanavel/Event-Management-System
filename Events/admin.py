from django.contrib import admin
from .forms import EventForm
from django.urls import path
from Events import views
from django.db import models
from django.contrib.admin import AdminSite

from .models import (
    Department,
    EventName,
    Event,
    Venue
)



admin.site.register(Department)
admin.site.register(EventName)
admin.site.register(Venue)

class EventAdmin(admin.ModelAdmin):
    form = EventForm
admin.site.register(Event,EventAdmin)


class EventCalendarDisplay(models.Model):

    class Meta:
        verbose_name_plural = 'Event Calendar Display'

class EventCalendarDisplayAdmin(admin.ModelAdmin):
    form = EventForm

    def get_urls(self):
        view_name = '{}_{}_changelist'.format(
            self.model._meta.app_label, self.model._meta.model_name)

        return [
            path('oel/', views.CalendarView.as_view(), name=view_name),
        ]
    def has_change_permission(self, request, obj=None):
        return False

    def has_delete_permission(self, request, obj=None):
        return False

    # to disable view and add you can do this 
    def has_view_permission(self, request, obj=None):
        return True

    def has_add_permission(self, request):
        return False

admin.site.register(EventCalendarDisplay,EventCalendarDisplayAdmin)

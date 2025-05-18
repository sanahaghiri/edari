from django.contrib import admin
from .models import *
# Register your models here.


class LeaveAdmin(admin.ModelAdmin):
    
    fields = [
        "user",
        "days_or_clock",
        "is_accept",
        "is_reject",
        "clock_leave_date",
        "days_start_date",
        "days_end_date",
        "clock_start_time",
        "clock_end_time",
        "description"
    ]

    list_display = [
        "is_accept",
        "is_reject",
        "description"
    ]

    # search_fields = ["first_name", "last_name", "person_code","phone_number"]


admin.site.register(LeaveModel, LeaveAdmin)
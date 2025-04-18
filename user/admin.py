from django.contrib import admin
from .models import *
# Register your models here.


class PersonelAdmin(admin.ModelAdmin):
    
    fields = [
        "person_code",
        "password",
        "first_name",
        "last_name",
        "phone_number",
        "access",
    ]

    list_display = [
        "person_code",
        "first_name",
        "last_name",
        "phone_number",
        "access",
    ]

    search_fields = ["first_name", "last_name", "person_code","phone_number"]


admin.site.register(PersonelModel, PersonelAdmin)
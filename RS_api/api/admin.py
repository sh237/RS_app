from django.contrib import admin

# Register your models here.
from .models import DateManage

@admin.register(DateManage)

class DateManageAdimin(admin.ModelAdmin):
    pass
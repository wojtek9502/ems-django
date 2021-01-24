from django.contrib import admin

# Register your models here.
from django.contrib import admin
from ems_api.models import EntranceExit


class EntranceExitAdmin(admin.ModelAdmin):
    readonly_fields = ('entrance_date', 'exit_date')

admin.site.register(EntranceExit, EntranceExitAdmin)
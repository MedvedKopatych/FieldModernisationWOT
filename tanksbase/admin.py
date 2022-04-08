from django.contrib import admin
from tanksbase.models import Tank


class TanksBaseAdmin(admin.ModelAdmin):
    list_display = ['name', 'tier', 'nation', 'type']
    search_fields = ['name', 'tier', 'nation', 'type']
    ordering_fields = ['name', 'tier', 'nation', 'type']
    list_filter = ['tier', 'nation', 'type']


admin.site.register(Tank, TanksBaseAdmin)

from django.contrib import admin

from .models import SingleEntry


class singleEntryAdmin(admin.ModelAdmin):
    # fieldsets = [
    #    (None, {'fields': ['name']}),
    #    ('Date information', {'fields': ['date']})
    # ]
    list_display = ('name', 'date', 'price', 'paid_by')


admin.site.register(SingleEntry, singleEntryAdmin)

# Register your models here.

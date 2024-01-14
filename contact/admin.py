from django.contrib import admin

# Register your models here.

from .models import Contact, FAQ


class FAQAdmin(admin.ModelAdmin):
    """
    Admin views for FAQs
    """
    list_display = (
        'question',
        'answer',
    )


admin.site.register(Contact)
admin.site.register(FAQ, FAQAdmin)

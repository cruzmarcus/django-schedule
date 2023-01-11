from django.contrib import admin

from contacts.models import Category, Contact


class ContactAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "name",
        "last_name",
        "phone",
        "email",
        "created_date",
        "category",
    )
    list_display_links = ("id", "name", "last_name")
    list_filter = ("name", "last_name")
    list_per_page = 10
    search_fields = ("name", "last_name")


admin.site.register(Category)
admin.site.register(Contact, ContactAdmin)

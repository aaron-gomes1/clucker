# Configuration of the admin interface for microblogs
from django.contrib import admin
from .models import User

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = [
        'username', 'first_name', 'last_name', 'email', 'is_active'
    ]

    def is_superuser():
        return True

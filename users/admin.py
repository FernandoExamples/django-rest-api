from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import User

# Register your models here.


class UserAdmin(BaseUserAdmin):
    readonly_fields = ('last_login', 'date_joined')
    fieldsets = (
        (None, {"fields": ("username", "password")}),
        ("Información Personal", {"fields": ("first_name", "last_name", "email")}),
        ("Redes Sociales", {"fields": ("web_site",)}),
        ("Permisos", {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        (None, {"fields": ("last_login", "date_joined")}),
    )


admin.site.register(User, UserAdmin)

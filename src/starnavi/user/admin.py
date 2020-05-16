from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import User


class CustomUserAdmin(UserAdmin):
    fieldsets = (
        ('Common', {'fields': ('username', 'email', 'is_staff')}),
        ('Important dates', {'fields': ('last_login', 'date_joined')})
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'email', 'password1', 'password2', 'is_staff')}),
    )
    readonly_fields = ('id', 'last_login', 'date_joined')

    list_display = ('id', 'username', 'email', 'is_staff', 'last_login', 'date_joined')
    list_filter = ('is_staff', 'last_login', 'date_joined')
    filter_horizontal = []
    search_fields = ('username', 'email')


admin.site.register(User, CustomUserAdmin)

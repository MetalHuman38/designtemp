from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.utils.translation import gettext as _
from core import models

# Register your models here.


class UserAdmin(BaseUserAdmin):
    """
    Custom user Admin class to handle user-related
    """

    ordering = ['id']

    list_display = ['email', 'fullname', 'is_staff', 'is_active']

    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        (_('Personal Info'), {'fields': ('fullname',)}),
        (_('Permissions'), {
         'fields': ('is_active', 'is_staff', 'is_superuser')}),
        (_('Important dates'), {'fields': ('last_login',)}),
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': (
                'email',
                'password1',
                'password2',
                'fullname',
                'is_active',
                'is_staff',
                'is_superuser',
            )
        }),
    )

    search_fields = ['email', 'fullname']

    list_filter = ['is_active', 'is_staff', 'is_superuser']

    readonly_fields = ['last_login']


admin.site.register(models.User, UserAdmin)

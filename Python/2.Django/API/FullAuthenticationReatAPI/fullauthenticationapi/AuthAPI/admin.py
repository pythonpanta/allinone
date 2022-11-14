from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from . models import User
from django.contrib.auth.models import Group
# Register your models here.
class UserAdmin(BaseUserAdmin):
    list_display = ('id','email', 'username', 'is_admin','is_staff')
    list_filter = ('is_admin','tc')
    fieldsets = (
        ('User Credential', {'fields': ('email', 'password')}),
        ('Personal info', {'fields': ('username','tc')}),
        ('Permissions', {'fields': ('is_admin',)}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'username','tc', 'password1', 'password2'),
        }),
    )
    search_fields = ('email',)
    ordering = ('email',)
    filter_horizontal = ()


# Now register the new UserAdmin...
admin.site.register(User, UserAdmin)
# ... and, since we're not using Django's built-in permissions,
# unregister the Group model from admin.
admin.site.unregister(Group)
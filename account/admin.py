from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from account.models import User


class UserModelAdmin(UserAdmin):
    model = User

    # The fields to be used in displaying the User model.
    # These override the definations on the base UserModelAdmin that reference specific fields on the auth.User.


    list_display = ["id", "email", "name", "is_active", "is_staff", "is_superuser", "is_customer", "is_seller"]
    list_filter = ["is_superuser"]
    fieldsets = [
        ("User Credentials", {"fields": ["email", "password"]}),
        ("Personal Information", {"fields": ["name", "city"]}),
        ("Permission", {"fields": ["is_active", "is_staff", "is_superuser", "is_customer", "is_seller", "groups", "user_permissions"]}),
        ]


    #It is not necessary.
    #add_fieldsets is not a standard ModelAdmin attribute. UserModelAdmin overrides get_fieldsets to use this attribute when creating user.
    #add_fieldsets is a list of tuples. Each tuple represents a section in Add User Form.

    add_fieldsets = [
        (
            #It is the title of the section. Setting this to None leave the section title blank.
            None,
        {
            #It's a css class to make full width admin layout.
            "classes": ["wide"],
            #This fields will appear in admin panel add user form
            "fields": ["email", "password1", "password2"]
        }
         )
    ]

    search_fields = ["email"]
    ordering = ["email", "id"]
    filter_horizontal = ["groups", "user_permissions"]

admin.site.register(User ,UserModelAdmin)

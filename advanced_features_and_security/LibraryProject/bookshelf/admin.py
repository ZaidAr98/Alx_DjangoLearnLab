
# Register your models here.
# from django.contrib import admin
# from .models import Book

# class BookAdmin(admin.ModelAdmin):
#     search_fields = ('title', 'author', 'publication_year')
#     list_filter = ('title', 'author','publication_year')

# admin.site.register(Book, BookAdmin)


from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser

class CustomUserAdmin(UserAdmin):
    model = CustomUser
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('date_of_birth', 'profile_photo')}),
    )

admin.site.register(CustomUser, CustomUserAdmin)
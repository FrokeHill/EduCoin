from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import User, Coins, Group, Item, Purchase, Transactions, News


@admin.register(User)
class UserAdmin(BaseUserAdmin):
    list_display = ['username', 'email', 'user_type', 'first_name', 'last_name', 'is_staff', 'is_superuser']
    list_filter = ['user_type', 'is_staff', 'is_superuser', 'is_active']
    
    fieldsets = BaseUserAdmin.fieldsets + (
        ('User Type', {'fields': ('user_type',)}),
        ('Student ma\'lumotlar', {'fields': ('t_yil', 'phone', 'phone2', 'profil_pic')}),
        ('Teacher ma\'lumotlar', {'fields': ('started_at',)}),
    )
    
    add_fieldsets = BaseUserAdmin.add_fieldsets + (
        ('Qo\'shimcha ma\'lumotlar', {
            'fields': ('email', 'user_type', 't_yil', 'phone', 'started_at')
        }),
    )
    
    search_fields = ['username', 'email', 'first_name', 'last_name']


@admin.register(Transactions)
class TransactionsAdmin(admin.ModelAdmin):
    list_display = ['student', 'amount', 'status', 'reason', 'created_at']
    list_filter = ['status', 'created_at']
    search_fields = ['student__username', 'reason']


@admin.register(Group)
class GroupAdmin(admin.ModelAdmin):
    list_display = ['name', 'teacher', 'created_at']
    list_filter = ['created_at']
    search_fields = ['name', 'teacher__username']
    filter_horizontal = ['students']


admin.site.register(Coins)
admin.site.register(Item)
admin.site.register(Purchase)
admin.site.register(News)
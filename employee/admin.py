from django.contrib import admin
from employee.models import Employee, Accessory


class EmployeeAdmin(admin.ModelAdmin):
    fields = ('name', 'surname', 'img')
    list_display = 'name', 'surname'
    list_filter = 'surname',


class AccessoryAdmin(admin.ModelAdmin):
    fields = ('owner', 'name', 'prise', 'img', 'comment')
    list_display = 'owner_name', 'name'
    list_filter = 'owner',


admin.site.register(Employee, EmployeeAdmin)
admin.site.register(Accessory, AccessoryAdmin)

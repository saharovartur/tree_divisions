from django.contrib import admin
from mptt.admin import DraggableMPTTAdmin

from department_employee.models import Department, Employee, Position


@admin.register(Department)
class DepartmentAdmin(DraggableMPTTAdmin):
    """
    Админ-панель модели отделов
    """
    prepopulated_fields = {'slug': ('title',)}


@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'department']


@admin.register(Position)
class PositionAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'department']




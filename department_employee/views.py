from django.views.generic import DetailView
from department_employee.models import Department

from django.shortcuts import render
from .models import Employee


def employee_list(request):
    """Список сотрудников"""
    employee_list = Employee.objects.all()
    return render(request, 'user_list.html', {'employee_list': employee_list})


def department_chain(request):
    """дерево отделов"""
    return render(request, 'department_list.html')


class DepartmentDetailView(DetailView):
    """детальная страница просмотра отдела"""
    model = Department
    template_name = 'department_detail.html'





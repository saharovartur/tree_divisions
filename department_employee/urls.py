from django.urls import path
from department_employee import views
from department_employee.views import DepartmentDetailView

urlpatterns = [
    path('', views.department_chain, name='department_chain'),
    path('employee_list/', views.employee_list, name='employee_list'),
    path('department_detail/<slug:slug>/', DepartmentDetailView.as_view(), name='department_detail')

]

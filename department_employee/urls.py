from django.urls import path
from department_employee import views
from department_employee.views import DepartmentChainDetailView

urlpatterns = [
    path('', views.department_chain, name='department_chain'),
    path('user-list/', views.employee_list, name='user_list'),
    path('department_detail/<slug:slug>/', DepartmentChainDetailView.as_view(), name='department_detail')

]

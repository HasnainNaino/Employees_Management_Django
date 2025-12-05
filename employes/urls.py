from django.urls import path
from . import views
urlpatterns = [
    path('create_employee/', views.create_employee, name='create_employee'),
    path('', views.employee_list, name='employee_list'),
    path('employees/update/<int:pk>/', views.update_employee, name='update_employee'),
    path('employees/delete/<int:pk>/', views.delete_employee, name='delete_employee'),
]  
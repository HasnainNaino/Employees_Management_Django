from django.shortcuts import render
from .models import Employee
from .forms import EmployeeForm
from django.shortcuts import redirect

def create_employee(request):
    if request.method == 'POST':
        form = EmployeeForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('employee_list')
    else:
        form = EmployeeForm()
    return render(request, 'create_employee.html', {'form': form})



def employee_list(request):
    employees = Employee.objects.all().order_by('-created_at', '-updated_at')
    return render(request, 'employee_list.html', {'employees': employees})  

def update_employee(request, pk):
    employee = Employee.objects.get(id=pk)
    if request.method == 'POST':
        form = EmployeeForm(request.POST, instance=employee)
        if form.is_valid():
            form.save()  # updated_at will auto-update here
            return redirect('employee_list')
    else:
        form = EmployeeForm(instance=employee)
    return render(request, 'update_employee.html', {'form': form, 'employee': employee})


def delete_employee(request, pk):
    employee = Employee.objects.get(id=pk)

    if request.method == 'POST':
        employee.delete()
        return redirect('employee_list')   # redirect should be inside POST

    return redirect('employee_list')

   



    

# Create your views here.

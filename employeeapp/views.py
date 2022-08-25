from django.shortcuts import render,redirect
from .forms import EmployeeForm
import openpyxl
from .models import *
# Create your views here.


def upload_file(request):
    if request.method == 'POST':
        form = EmployeeForm(request.POST, request.FILES)
        if form.is_valid():
            file = request.FILES['file']
        wb = openpyxl.load_workbook(file)
        worksheet = wb.active
        objs = list()
        for row in worksheet.iter_rows(min_row=2):
            row_data = list()
            for cell in row:
                row_data.append(str(cell.value))
            if not Employee.objects.filter(id=row_data[0]).exists():
                department=Department.objects.filter(department=row_data[5]).values('id')
                obj=Employee(id=row_data[0],name=row_data[1],salary=row_data[2],email=row_data[3],phone=row_data[4],department_id=department)
                objs.append(obj)
        Employee.objects.bulk_create(objs)


    else:
        form = EmployeeForm()
    return render(request, 'home.html', {'form': form})

def view(request):
    object_list = list(Employee.objects.all().values('id', 'name', 'salary', 'email', 'phone','department__department'))
    return render(request, 'index.html', {'object_list': object_list})




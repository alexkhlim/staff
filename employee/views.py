from django.shortcuts import render
import employee.models as mo
from employee.forms import EmployeeForm, AccessoryForm


def main_page(request):
    employees = mo.Employee.objects.all()
    return render(request, 'main_page.html', context={'employees': employees})


def empl(request, id):
    sotr = mo.Employee.objects.get(id=id)
    accs = mo.Accessory.objects.filter(owner_id=id)
    return render(request, 'employee.html', context={'sotr': sotr, 'accs': accs})


def create_empl(request):
    if request.POST:
        form = EmployeeForm(request.POST, request.FILES or None)
        form.is_valid()
        form.save()
    return render(request, 'create_empl.html', context={'form': EmployeeForm()})


def create_acc(request, id):
    if request.POST:
        mo.Accessory.objects.create(
            owner=mo.Employee.objects.get(id=id),
            name=request.POST.get('name'),
            prise=request.POST.get('prise'),
            comment=request.POST.get('comment'),
            img=request.FILES.get('img')
        )
        # form = AccessoryForm(request.POST)
        # form.is_valid()
        # form.save()
    return render(request, 'create_acc.html')#, context={'form': AccessoryForm()})

from django.http.response import Http404, HttpResponse
from django.shortcuts import render
from Product.models import Employees
from django.shortcuts import get_object_or_404


def home_view(request):
    employees = Employees.objects.all()
    context = {'employees': employees}
    return render(request, 'employeelist.html', context)


def empDetails(request, id):
    emp_details = Employees.objects.get(id=id)
    # try:
    #     # emp_details = get_object_or_404(Employees, id=id)
    #     emp_details = Employees.objects.get(id=id)
    # except Employees.DoesNotExist:
    #     raise Http404
    context = {'emp_details': emp_details}
    return render(request, 'employeeDetails.html', context)


def contact(request):
    return render(request, 'contact.html')


def about(request):
    return render(request, 'about.html')


def login(request):
    return render(request, 'login.html')

def register(request):
    return render(request, 'register.html')
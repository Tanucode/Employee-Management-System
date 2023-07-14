from django.shortcuts import render,redirect
from .models import Role, Employee
from django.contrib import messages
from django.contrib.auth.models import User,auth

def login(request):
    if request.method == 'POST':
        fullname = request.POST['fullname']
        dob = request.POST['dob']
        print(dob)

        if Employee.objects.filter(username= fullname).exists():
            if str(dob) == str(Employee.objects.get(username=fullname).dob):
                messages.info(request,"Logged in Succussfully!!")
                return redirect('/')
            else:
                messages.info(request,"Dob inccorect!!")
        else:
            messages.info(request,"Employee Name doesn't exist ")
        return redirect('/login')
    return render(request,'Login.html')

def home(request):
    return render(request,'home.html')

def register(request):
    if request.method == 'POST':
        fullname = request.POST['fullname']
        email = request.POST['email']
        empID = request.POST['empID']
        phone = request.POST['phone']
        # password = request.POST['password']
        desig = request.POST['desig']
        salary = request.POST['salary']
        yoa = request.POST['yoa']
        skill = request.POST['skill']
        aoa = request.POST['aoa']
        dob = request.POST['dob']
        gender = request.POST['gender']
        address = request.POST['address']
        state = request.POST['state']
        city = request.POST['city']
        region = request.POST['region']
        pin = request.POST['pin']

        addr = address + ", " + state + ", " + city + ", " + region + ", " + pin

        roleID = Role.objects.get(name=aoa)

        new_emp = Employee.objects.create(username=fullname,email=email,empid=empID,desig=desig,salary=salary,exp=yoa,skill=skill,aow=roleID,phone=phone,dob=dob,gender=gender,address=addr)
        new_emp.save()

        return redirect('/login')

    roles = Role.objects.all()
    states = ['Arunachal Pradesh','Andhra Pradesh','Assam']
    return render(request,'register.html',{'states':states,'roles':roles})

def  adminhome(request):
    return render(request,'adminhome.html')

def panel(request):
    if request.method == 'POST':
        admin = request.POST['admin']
        password = request.POST['password']

        user = auth.authenticate(username=admin,password=password)

        if user is not None:
            messages.info(request,"Admin Logged Successfully!!")
            return redirect('/adminhome')
        else:
            messages.info(request,"Invalid Credentials")
            return redirect('/panel')
    return render(request,'panel.html')

def searchEmployee(request):

        
        return render(request,'searchEmployee.html')

def services(request):
    return render(request,'services.html')

def contactus(request):
    return render(request,'contactus.html')

def about(request):
    return render(request,'about.html')


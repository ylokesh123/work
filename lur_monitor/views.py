from django.shortcuts import render,redirect
from .models import *
from .forms import *
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from django.contrib.auth.models import User
import json
# Create your views here.
def dash_week_me(req):
    return render(req,"me_week.html")

def dash_week_all(req):
    return render(req,"weekly.html")

def dash_month_me(req):
    return render(req,"me_month.html")

def dash_month_all(req):
    return render(req,"monthly.html")

def dash_current_me(req):
    return render(req,"current_me.html")

def dash_current_all(req):
    return render(req,"current_all.html")

def screenshot(req,id):
     if id == 0:
        employee = Employee.objects.all()
     else:
        empid = empId.objects.get(id=id)
        employee = Employee.objects.filter(id=id)
     allempid = empId.objects.all()
     return render(req,"screenshot.html",locals())

def apps(req,id):
     if id == 0:
        employee = Employee.objects.all()
     else:
        empid = empId.objects.get(id=id)
        employee = Employee.objects.filter(id=id)
     allempid = empId.objects.all()
     return render(req,"Apps.html",locals())

def urls(req,id):
    if id == 0:
        employee = Employee.objects.all()
    else:
        empid = empId.objects.get(id=id)
        employee = Employee.objects.filter(id=id)
    allempid = empId.objects.all()
    return render(req,"URL.html",locals())


def Viewtsheet(req,id):
     if id == 0:
        employee = Employee.objects.all()
     else:
        empid = empId.objects.get(id=id)
        employee = Employee.objects.filter(id=id)
     allempid = empId.objects.all()
     return render(req,"Timesheet.html",locals())


def approvetsheet(req):
    emp = Employee.objects.all()
    return render(req,"Approve.html",{'emp':emp})

def attendence(req,id):
    if id == 0:
        employee = Employee.objects.all()
    else:
        empid = empId.objects.get(id=id)
        employee = Employee.objects.filter(id=id)
    allempid = empId.objects.all()
    return render(req,"Attedence.html",locals())
    

def members(req):
    return render(req,"Member.html")

def teams(req):
    return render(req,"Teams.html")

def project(req,id):
     if id == 0:
        project = Project.objects.all()
     else:
        status = Proj_status.objects.get(id=id)
        project = Project.objects.filter(id=id)
     allstatus = Proj_status.objects.all()
     return render(req,"project.html",locals())

def todo(req):
    return render(req,"todo.html")

def client(req):
    client = clients.objects.all()
    return render(req, "client.html", {'client':client})

def jobsite(req):
    return render(req,"JobSites.html")

def schedules(req):
    return render(req,"Schedule.html")

def timeoff(req):
    return render(req,"timeoff.html")

def time_act(req):
    return render(req,"time_activity.html")

def weekly(req):
    return render(req,"week.html")

def dynmic_rep(req):
    return render(req,"Dynamicreport.html")

def all_report(req):
    return render(req,"report.html")

def general(req):
    return render(req,"general.html")

def features(req):
    return render(req,"feature.html")

def subscription(req):
    return render(req,"Subscription.html")

def organization(req):
     companies = Company.objects.all()
     return render(req,"Organization.html",{'companies':companies})

def all_settings(req):
    return render(req,"allsettings.html")

def integration(req):
    return render(req,"intigration.html")

def change_log(req):
    return render(req,"changelog.html")

def help_desk(req):
    return render(req,"Helpdesk.html")


def Login(request):
    msg = None
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        try:
            if user.is_staff:
                login(request, user)
                msg = "login successfully"
                return redirect('dash_current_me')
            else:
                msg = "Invalid Credentials"
        except:
            msg = "Invalid Credentials"
    dic = {'msg': msg}
    return render(request, 'login.html', dic)


def Alogout(request):
    logout(request)
    messages.success(request, "Logout Successfully")
    return redirect('Login')


def register(req):
    pass

def profile(req):
    return render(req,"profile.html")

def privacy(req):
    return render(req,"privacy.html")


def comp(request):
    if request.method == "POST":

        form = CompanyForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect("/show")
            except:
                pass
                
    else:
        form = CompanyForm()
    return render(request, "comp.html", {'form':form})

# To retrieve Company details
def show(request):
    companies = Company.objects.all()
    return render(request, "show.html", {'companies':companies})

# To Edit Company details
def edit(request, cName):
    company = Company.objects.get(cName=cName)
    return render(request, "edit.html", {'company':company})

# To Update Company
def update(request, cName):
    company = Company.objects.get(cName=cName)
    form = CompanyForm(request.POST, instance= company)
    if form.is_valid():
        form.save()
        return redirect("/show")
    return render(request, "edit.html", {'company': company})

# To Delete Company details
def delete(request, cName):
    company = Company.objects.get(cName=cName)
    company.delete()
    return redirect("/show")


# To create employee
def emp(request):
    if request.method == "POST":

        form = EmployeeForm(request.POST)
        if form.is_valid():
            try:
                
                form.save()
                return redirect("/showemp")
            except:
                pass
    else:
        form = EmployeeForm()
    return render(request, "addemp.html", {'form':form})

# To show employee details
def showemp(request):
    employees = Employee.objects.all()
    return render(request, "showemp.html", {'employees':employees})

# To delete employee details
def deleteEmp(request, eFname):
    employee = Employee.objects.get(eFname=eFname)
    employee.delete()
    return redirect("/showemp")

# To edit employee details
def editemp(request, eFname):
    employee = Employee.objects.get(eFname=eFname)
    return render(request, "editemployee.html", {'employee':employee})

# To update employee details
def updateEmp(request, eFname):
    employee = Employee.objects.get(eFname=eFname)
    form = EmployeeForm(request.POST, instance= employee)
    print('Hello1')
    if form.is_valid():
        
        form.save()
        return redirect("/showemp")
    return render(request, "editemployee.html", {'employee': employee})

def add_client(request):
    if request.method == "POST":

        form = clientForm(request.POST)
        if form.is_valid():
            try:
                
                form.save()
                return redirect("/clients")
            except:
                pass
    else:
        form = clientForm()
    return render(request, "add_clients.html", {'form':form})
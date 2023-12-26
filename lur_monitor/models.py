from django.db import models
from .models import *
# Create your models here.

class Company(models.Model):
    cName = models.CharField(max_length=50)
    cEmail = models.EmailField()
    cLogo = models.ImageField(upload_to="media", blank=True, null=True)
    cUrl = models.CharField(max_length=50)
    class Meta:
        db_table = "company"
    def __str__(self):
      return self.cName


class Role(models.Model):
     role = models.CharField(max_length=50,default=0)
     class Meta:
        db_table = "Role"
     def __str__(self):
      return self.role
     
class empId(models.Model):
    Empid = models.CharField(max_length=50)
    created = models.DateTimeField(auto_now_add=True)
    class Meta:
        db_table = "empId"
    def __str__(self):
     return self.Empid

class Employee(models.Model):
    eFname = models.CharField(max_length=50,unique='true')
    eLname = models.CharField(max_length=50)
    eCompany = models.ForeignKey(Company, on_delete=models.CASCADE,default=0)
    empRole = models.ForeignKey(Role, on_delete=models.CASCADE, default=0)
    empId = models.ForeignKey(empId, on_delete=models.CASCADE,default=0)
    eEmail = models.EmailField(max_length=50)
    screenshot= models.FileField(upload_to="media", blank=True, null=True)
    url = models.URLField(max_length=200,null=True)
    apps = models.CharField(max_length=100,null=True)
    ePhone = models.CharField(max_length=50,null=True)
    created = models.DateTimeField(auto_now_add=True)
    app_img = models.FileField(upload_to="media", blank=True, null=True)
    class Meta:
        db_table = "employee"
    def __str__(self):
     return self.eFname

class Proj_status(models.Model):
     status = models.CharField(max_length=50)
     class Meta:
        db_table = "Proj_status"
     def __str__(self):
      return self.status
    

class clients(models.Model):
         pname = models.CharField(max_length=50,default=0)
         client = models.CharField(max_length=50)
         eCompany = models.ForeignKey(Company, on_delete=models.CASCADE)
         pro_type = models.ForeignKey(Role,on_delete=models.CASCADE)
         employee =models.ForeignKey(Employee, on_delete=models.CASCADE)
         class Meta:
            db_table = "clients"
         def __str__(self):
          return self.client   
 
class Project(models.Model):
         project= models.CharField(max_length=50,default=0)
         eCompany = models.ForeignKey(Company, on_delete=models.CASCADE)
         employee =models.ForeignKey(Employee, on_delete=models.CASCADE)
         pclient = models.ForeignKey(clients, on_delete=models.CASCADE,default=0)
         ePhone = models.CharField(max_length=50)
         status = models.ForeignKey(Proj_status, on_delete=models.CASCADE,default=0)
         class Meta:
            db_table = "Project"  
         def __str__(self):
          return self.project   




    
#class Login(models.Model):
    #UserName = models.CharField(max_length=50)
    #password = models.CharField(max_length=32)
    #class Meta:
        #db_table = "login"





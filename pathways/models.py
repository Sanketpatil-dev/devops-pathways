from django.db import models

# Create your models here.

class contactus(models.Model):
    id= models.AutoField(primary_key=True, null=False)
    name= models.CharField(max_length=50)
    contact=models.CharField(max_length=13)
    email= models.CharField(max_length=20)
    message= models.CharField(max_length=150)


    def __str__(self):
        return f'{self.name} {self.contact} {self.email} {self.message}'

class bookticket(models.Model):
    id= models.AutoField(primary_key=True, null=False)
    pname= models.CharField(max_length=50)
    pemail= models.CharField(max_length=30)
    pnum= models.CharField(max_length=13)
    clocation= models.CharField(max_length=20)
    destination= models.CharField(max_length=20)
    sdate= models.DateField()
    adults= models.CharField(max_length=3)
    child= models.CharField(max_length=3)

    def __str__(self):
        return f'{self.pname} {self.pemail} {self.pnum} {self.clocation} {self.destination} {self.sdate} {self.adults} {self.child}'

class signup(models.Model):
    id= models.AutoField(primary_key=True, null=False)
    fname= models.CharField(max_length=50)
    lname= models.CharField(max_length=30)
    phnum= models.CharField(max_length=13)
    emailid= models.CharField(max_length=20)
    pswd= models.CharField(max_length=20)
    
    def __str__(self):
        return f'{self.fname} {self.lname} {self.phnum} {self.emailid} {self.pswd}'


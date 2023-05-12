from django.db import models

# Create your models here.

class Visitor(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(blank=True, null=True)
    phone = models.CharField(max_length=20, blank=True, null=True)
    address = models.CharField(max_length=100)
    company = models.CharField(max_length=50, blank=True, null=True)
    purpose = models.CharField(max_length=100, blank=True,null=True)
    check_in = models.DateTimeField(blank=True, null=True, auto_now_add=True)
    check_out = models.DateTimeField(blank=True, null=True)
    host = models.CharField(max_length=100,blank=True, null=True)

class ExcelFile(models.Model):
    file=models.FileField(upload_to='excel')
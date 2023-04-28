from django.db import models

# Create your models here.

class Visitor(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(blank=True, null=True)
    phone = models.CharField(max_length=20, blank=True, null=True)
    address = models.CharField(max_length=100)
    company = models.CharField(max_length=50, blank=True, null=True)

class Purpose(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=200)


class Host(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(blank=True, null=True)
    phone = models.CharField(max_length=20, blank=True, null=True)

class VisitDetails(models.Model):
    visitor = models.ForeignKey(Visitor, on_delete=models.CASCADE)
    host = models.ForeignKey(Host, on_delete=models.CASCADE)
    check_in = models.DateTimeField(blank=True, null=True)
    check_out = models.DateTimeField(blank=True, null=True)
    location = models.CharField(max_length=50, blank=True, null=True)
    status = models.CharField(max_length=10, blank=True, null=True)


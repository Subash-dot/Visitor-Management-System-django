from django.db import models
from django.utils.text import slugify

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


class Purpose(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField()
    slug = models.SlugField(unique=True,blank=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super(Purpose,self).save(*args, **kwargs)

    def __str__(self):
        return self.title

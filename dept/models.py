from django.db import models

# Create your models here.
class Faculty(models.Model):
    faculty_id=models.AutoField(primary_key=True)
    header_image = models.ImageField(blank=True, null=True, upload_to="images/")
    Username=models.CharField(max_length=100,unique=True)
    FirstName=models.CharField(max_length=100)
    LastName=models.CharField(max_length=100)
    Email=models.EmailField(max_length=200)
    Password=models.CharField(max_length=100)
    
    def __str__(self):
        return self.FirstName


# class committee(models.Model):
#     Username=models.CharField(unique=True,max_length=100)
#     Password=models.CharField(max_length=100, null=False)

#     def __str__(self):
#         return self.Username


class Emf(models.Model):
    title = models.CharField(max_length=100)
    cie_image = models.ImageField(null=True, blank=True, upload_to="images/")

class emfdisplay(models.Model):
    name = models.CharField(max_length = 255)
    comments = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

class cn(models.Model):
    cn_title = models.CharField(max_length=100)
    cn_cie_image = models.ImageField(null=True, blank=True, upload_to="images/")

class cndisplay(models.Model):
    name = models.CharField(max_length = 255)
    comments_cn = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

class ml(models.Model):
    ml_title = models.CharField(max_length=100)
    ml_cie_image = models.ImageField(null=True, blank=True, upload_to="images/")

class mldisplay(models.Model):
    name = models.CharField(max_length = 255)
    comments_ml = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

class ws(models.Model):
    ws_title = models.CharField(max_length=100)
    ws_cie_image = models.ImageField(null=True, blank=True, upload_to="images/")

class wsdisplay(models.Model):
    name = models.CharField(max_length = 255)
    comments_ws = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

class iot(models.Model):
    iot_title = models.CharField(max_length=100)
    iot_cie_image = models.ImageField(null=True, blank=True, upload_to="images/")

class iotdisplay(models.Model):
    name = models.CharField(max_length = 255)
    comments_iot = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)


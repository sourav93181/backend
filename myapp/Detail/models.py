from django.db import models
class Detail(models.Model):
    companyId=models.AutoField(primary_key=True)
    
    companyName = models.CharField(max_length=250)
    companyDescription=models.CharField(max_length=10000)
    officalLink=models.CharField(max_length=10000)
    desgination=models.CharField(max_length=50)
    website = models.CharField(max_length=250)
    location = models.CharField(max_length=250)
    jobType = models.CharField(max_length=250)
    experience = models.CharField(max_length=250)
    qualification = models.CharField(max_length=250)
    Batch = models.CharField(max_length=250)
    salary = models.CharField(max_length=250)
    # required skills
    point1=models.CharField(max_length=250)
    point2=models.CharField(max_length=250)
    point3=models.CharField(max_length=250)
    point4=models.CharField(max_length=250)
    point5=models.CharField(max_length=250)
    
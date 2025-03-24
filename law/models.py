from django.db import models

class Services(models.Model):
    image = models.ImageField(upload_to='images/%Y/%m/%d/')
    title = models.CharField(max_length=20)
    prah = models.CharField(max_length=100)

    def __str__(self):
        return self.title



class SumData(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=100)
    phone = models.CharField(max_length=12)
    subject = models.CharField(max_length=20) 
    message = models.TextField(max_length=500)  

    def __str__(self):
        return self.name

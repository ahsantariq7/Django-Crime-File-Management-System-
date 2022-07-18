from django.db import models



# Create your models here.
class Contact(models.Model):
    name=models.CharField( max_length=120)
    email=models.CharField(max_length=120)
    phone=models.CharField(max_length=120)
    desc=models.TextField()
    date=models.DateField()

    def __str__(self):
        return self.name
    

class AddMissingPerson(models.Model):
    title = models.TextField()
    cover = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.title

class ShowMostWantedPerson(models.Model):
    title = models.TextField()
    cover = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.title


class FIR(models.Model):
    name=models.CharField( max_length=120)
    email=models.CharField(max_length=120)
    phone=models.CharField(max_length=120)
    reason=models.TextField()
    date=models.DateField()

    def __str__(self):
        return self.name


class Crime(models.Model):
    name=models.CharField( max_length=120)
    email=models.CharField(max_length=120)
    phone=models.CharField(max_length=120)
    crime=models.TextField()
    address=models.TextField()
    date=models.DateField()

    def __str__(self):
        return self.name

class AddComplaint(models.Model):
    name=models.CharField( max_length=120)
    email=models.CharField(max_length=120)
    phone=models.CharField(max_length=120)
    complaint=models.TextField()
    address=models.TextField()
    date=models.DateField()

    def __str__(self):
        return self.name
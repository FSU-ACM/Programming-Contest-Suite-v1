from django.db import models

class Admin(models.Model):
    """
    """
    AdminID = models.AutoField(primary_key=True)
    UserName = models.CharField(max_length=30)
    Password = models.CharField(max_length=60)

class Faculty(models.Model):
    """
    """
    FacultyID = models.AutoField(primary_key=True)
    FirstName = models.CharField(max_length=30)
    LastName = models.CharField(max_length=30)
    Email = models.CharField(max_length=30)
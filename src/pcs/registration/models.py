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

class Course(models.Model):
    """
    """
    CourseID = models.AutoField(primary_key=True)
    Faculty = models.ForeignKey('Faculty', on_delete=models.CASCADE)
    CourseName = models.CharField(max_length=60)

class Account(models.Model):
    """
    """
    AccountID = models.AutoField(primary_key=True)
    Role = models.CharField(max_length=30, null=True)
    FirstName = models.CharField(max_length=30)
    LastName = models.CharField(max_length=30)
    FsuNum = models.CharField(max_length=10)
    FsuID = models.CharField(max_length=10)
    Email = models.CharField(max_length=30)
    Password = models.CharField(max_length=60)
    Team = models.ForeignKey('Team', on_delete=models.CASCADE, null=True)
    Course = models.ForeignKey('Course', on_delete=models.CASCADE, null=True)

class Team(models.Model):
    """
    """
    DivisionChoices = (('L', 'Lower Division'),
                       ('U', 'Upper Division'))

    TeamID = models.AutoField(primary_key=True)
    TeamName = models.CharField(max_length=30)
    Division = models.CharField(max_length=1, 
                                choices=DivisionChoices)
    Password = models.CharField(max_length=60)
    Leader = models.OneToOneField('Account', on_delete=models.CASCADE)
    Members = models.CharField(max_length=150)

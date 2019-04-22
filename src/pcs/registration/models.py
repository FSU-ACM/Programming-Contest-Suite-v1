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
    Faculty = models.ForeignKey(Faculty, on_delete=models.SET_NULL, null=True)
    CourseName = models.CharField(max_length=60)

class Team(models.Model):
    """
    """
    
    DIVISION = (
        ('L', 'Lower Division'),
        ('U', 'Upper Division')
    )

    TeamID = models.AutoField(primary_key=True)
    TeamName = models.CharField(max_length=30)
    Division = models.CharField(max_length=1, choices=DIVISION)
    Password = models.CharField(max_length=60)
    Members = models.CharField(max_length=150)
    Leader = models.OneToOneField('Account', on_delete=models.CASCADE, null=True)

class Account(models.Model):
    """
    """
    
    ROLE = (
        ('P', 'Participant'),
        ('Q', 'Question Writer'),
        ('V', 'Volunteer')
    )

    AccountID = models.AutoField(primary_key=True)
    Role = models.CharField(max_length=1, choices=ROLE, null=True)
    FirstName = models.CharField(max_length=30)
    LastName = models.CharField(max_length=30)
    FsuNum = models.CharField(max_length=10)
    FsuID = models.CharField(max_length=10)
    Email = models.CharField(max_length=30)
    Password = models.CharField(max_length=250)
    isSignedIn = models.BooleanField(default=False)
    Team = models.ForeignKey(Team, on_delete=models.SET_NULL, null=True)
    Course = models.ForeignKey(Course, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return str(self.FirstName, ' ', self.LastName)
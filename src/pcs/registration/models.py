from django.db import models

class Admin(models.Model):
    """
    Admin Model
    """
    AdminID = models.AutoField(primary_key=True)
    UserName = models.CharField(max_length=30)
    Password = models.CharField(max_length=60)

class Faculty(models.Model):
    """
    Faculty Model
    - Faculty added manually at this point in time
    """
    FacultyID = models.AutoField(primary_key=True)
    FirstName = models.CharField(max_length=30)
    LastName = models.CharField(max_length=30)
    Email = models.CharField(max_length=30)

class Course(models.Model):
    """
    Course Model
    - Courses added manually at the this point in time
    """
    CourseID = models.AutoField(primary_key=True)
    Faculty = models.ForeignKey(Faculty, on_delete=models.SET_NULL, null=True)
    CourseName = models.CharField(max_length=60)

class Team(models.Model):
    """
    Team Model
    - Each team name is unique and has a one-to-one relation to the account that created it
    - Members field will be seperated by '\n' for DOMJudge
    """

    DIVISION = (
        ('L', 'Lower Division'),
        ('U', 'Upper Division')
    )

    TeamID = models.AutoField(primary_key=True)
    TeamName = models.CharField(max_length=30, unique=True)
    Division = models.CharField(max_length=1, choices=DIVISION)
    Password = models.CharField(max_length=60)
    Members = models.CharField(max_length=150)
    MemberIDs = models.CharField(max_length=30)
    Count = models.IntegerField(default=1)
    Leader = models.OneToOneField('Account', on_delete=models.SET_NULL, null=True)

class Account(models.Model):
    """
    Account Model
    - FSU Num, FSUID, and Email are all unique and are viable options for querying for an account
    - Foreign keys: Team account belongs to, and course the user has added
    - Password in db will be hashed and in unicode form. it will need to be decoded to bytes to be authenticated.
    - isCheckedIn (boolean) is for check in purposes on contest day
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
    FsuNum = models.CharField(max_length=10, unique=True)
    FsuID = models.CharField(max_length=10, unique=True)
    Email = models.CharField(max_length=30, unique=True)
    Password = models.CharField(max_length=250)
    isCheckedIn = models.BooleanField(default=False)
    Team = models.ForeignKey(Team, on_delete=models.SET_NULL, null=True)
    course_id = models.ManyToManyField(Course)
    def __str__(self):
        return str(self.FirstName, ' ', self.LastName)

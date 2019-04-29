from registration.models import Account, Course

def makeCourseList(aID=None):
    courses = getCourses(aID)
    return [(x.CourseID, x.CourseName) for x in courses]

def getCourses(aID):
    if aID is None:
        return Course.objects.all()
    else:
        return Course.objects.filter(account=aID)
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
CATEGORY_CHOICES = (
    ('web development','WEB DEVELOPMENT'),
    ('ml', 'ML'),
    ('ai','AI'),
)
class CourseUpload(models.Model):
    coursetitle = models.CharField(max_length=50, blank=True, null=True)
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES, default='pending')
    uploadedby = models.CharField(max_length=50, blank=True, null=True)
    coursedesc = models.CharField(max_length=10000, blank=True, null=True)
    courselink = models.CharField(max_length=100, blank=True, null=True)
    dateadded = models.DateField(blank=True, null=True,auto_now_add=True)
    thumbnailcourse = models.ImageField(upload_to='images/', default='images/defaultthumbnail.jpeg')
    def __str__(self):
        return self.coursetitle
class ExperienceUpload(models.Model):
    studentname = models.CharField(max_length=50, blank=True, null=True)
    branch = models.CharField(max_length=20, blank=True, null=True)
    passoutyear = models.CharField(max_length=50, blank=True, null=True)
    companyplaced = models.CharField(max_length=100, blank=True, null=True)
    experience = models.CharField(max_length=500,blank=True, null=True)
    def __str__(self):
        return self.studentname
class JobUpload(models.Model):
    companyname = models.CharField(max_length=50, blank=True, null=True)
    post = models.CharField(max_length=20, blank=True, null=True)
    vacantseats = models.CharField(max_length=50, blank=True, null=True)
    jobdesc = models.CharField(max_length=500, blank=True, null=True)
    location = models.CharField(max_length=500, blank=True, null=True)
    education = models.CharField(max_length=500, blank=True, null=True)
    def __str__(self):
        return self.companyname



class RegisterCourse(models.Model):
    coursename = models.CharField(max_length=50,blank=True, null=True)
    registeredby = models.CharField(max_length=50, blank=True, null=True)
    form_submitted = models.BooleanField(default=False)
    def __str__(self):
        return self.coursename


class Question(models.Model):
    author = models.ForeignKey(User, null=False, on_delete=models.CASCADE)
    title = models.CharField(max_length=200, null=False)
    body = models.TextField(null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.title
    def get_responses(self):
        return self.responses.filter(parent=None)
class Response(models.Model):
    user = models.ForeignKey(User, null=False, on_delete=models.CASCADE)
    question = models.ForeignKey(Question, null=False, on_delete=models.CASCADE, related_name='responses')
    parent = models.ForeignKey('self', null=True, blank=True, on_delete=models.CASCADE)
    body = models.TextField(null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.body

    def get_responses(self):
        return Response.objects.filter(parent=self)

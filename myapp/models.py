from django.db import models
from django.contrib.auth.models import User

# Create your models here.
CATEGORY_CHOICES = (
    ('----','----'),
    ('design','DESIGN'),
    ('development','DEVELOPMENT'),
    ('marketing','MARKETING'),
    ('it and software','IT AND SOFTWARE'),
    ('personal development','PERSONAL DEVELOPMENT'),
    ('business','BUSINESS'),
    ('photography','PHOTOGRAPHY'),
    ('music','MUSIC'),
)
PODCAST_CATEGORY = (
    ('----','----'),
    ('educational','EDUCATIONAL'),
    ('general', 'GENERAL'),
    ('others','OTHERS'),
)
USER_TYPE = (
    ('-----','-----'),
    ('student','STUDENT'),
    ('teacher', 'TEACHER'),
    ('alumni', 'ALUMNI'),
)

class UserProfile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    usertype = models.CharField(max_length=20, choices=USER_TYPE, default='-----')
    def __str__(self):
        return self.user.username

class CourseUpload(models.Model):
    coursetitle = models.CharField(max_length=50, blank=True, null=True)

    courseinstructorpicture = models.ImageField(upload_to='images/courses/instructors', default='images/defaultthumbnail.jpeg')
    courseinstructor = models.CharField(max_length=50, blank=True, null=True)
    aboutcourseinstructor = models.TextField(max_length=5000, blank=True, null=True)
    courseprerequisites = models.TextField(max_length=5000, blank=True, null=True)

    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES, default='----')
    uploadedby = models.CharField(max_length=50, blank=True, null=True)
    coursedesc = models.TextField(max_length=10000, blank=True, null=True)
    modulelink1 = models.CharField(max_length=100, blank=True, null=True)
    modulename1 = models.CharField(max_length=100, blank=True, null=True)
    modulelink2 = models.CharField(max_length=100, blank=True, null=True)
    modulename2 = models.CharField(max_length=100, blank=True, null=True)
    modulelink3 = models.CharField(max_length=100, blank=True, null=True)
    modulename3 = models.CharField(max_length=100, blank=True, null=True)
    modulelink4 = models.CharField(max_length=100, blank=True, null=True)
    modulename4 = models.CharField(max_length=100, blank=True, null=True)
    modulelink5 = models.CharField(max_length=100, blank=True, null=True)
    modulename5 = models.CharField(max_length=100, blank=True, null=True)
    modulelink6 = models.CharField(max_length=100, blank=True, null=True)
    modulename6 = models.CharField(max_length=100, blank=True, null=True)
    modulelink7 = models.CharField(max_length=100, blank=True, null=True)
    modulename7 = models.CharField(max_length=100, blank=True, null=True)
    modulelink8 = models.CharField(max_length=100, blank=True, null=True)
    modulename8 = models.CharField(max_length=100, blank=True, null=True)
    modulelink9 = models.CharField(max_length=100, blank=True, null=True)
    modulename9 = models.CharField(max_length=100, blank=True, null=True)
    modulelink10 = models.CharField(max_length=100, blank=True, null=True)
    modulename10 = models.CharField(max_length=100, blank=True, null=True)
    
    dateadded = models.DateField(blank=True, null=True,auto_now_add=True)
    thumbnailcourse = models.ImageField(upload_to='images/', default='images/defaultthumbnail.jpeg')
    def __str__(self):
        return self.coursetitle
class PodcastUpload(models.Model):
    podcasttitle = models.CharField(max_length=50, blank=True, null=True)
    podcastcategory = models.CharField(max_length=20, choices=PODCAST_CATEGORY, default='----')
    podcastspeaker = models.CharField(max_length=50, blank=True, null=True)
    podcastdesc = models.TextField(max_length=10000, blank=True, null=True)
    organisationofspeaker = models.CharField(max_length=100, blank=True, null=True)
    podcastdateadded = models.DateField(blank=True, null=True,auto_now_add=True)
    podcastthumbnail = models.ImageField(upload_to='images/podcast', default='images/defaultthumbnail.jpeg')
    podcastaudiofile = models.FileField(upload_to ='podcasts/audios')
    def __str__(self):
        return self.podcasttitle
class ExperienceUpload(models.Model):
    studentphoto = models.ImageField(upload_to='images/', default='images/defaultthumbnail.jpeg')
    studentname = models.CharField(max_length=50, blank=True, null=True)
    studentcollege = models.CharField(max_length=50, blank=True, null=True)
    branch = models.CharField(max_length=20, blank=True, null=True)
    passoutyear = models.CharField(max_length=50, blank=True, null=True)
    companyplaced = models.CharField(max_length=100, blank=True, null=True)
    experience = models.TextField(max_length=20000,blank=True, null=True)
    def __str__(self):
        return self.studentname
class JobUpload(models.Model):
    companyname = models.CharField(max_length=50, blank=True, null=True)
    post = models.CharField(max_length=20, blank=True, null=True)
    vacantseats = models.CharField(max_length=50, blank=True, null=True)
    jobdesc = models.TextField(max_length=500, blank=True, null=True)
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

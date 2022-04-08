from django.contrib import admin
from .models import CourseUpload, RegisterCourse, ExperienceUpload, Question, Response, JobUpload, UserProfile, PodcastUpload
# Register your models here.
class CourseUploadAdmin(admin.ModelAdmin):
    list_display = ('coursetitle','category','uploadedby','coursedesc','dateadded','thumbnailcourse','modulelink1','modulename1','modulelink2','modulename2','modulelink3','modulename3','modulelink4','modulename4','modulelink5','modulename5','modulelink6','modulename6','modulelink7','modulename7','modulelink8','modulename8','modulelink9','modulename9','modulelink10','modulename10','courseinstructorpicture','courseinstructor','aboutcourseinstructor','courseprerequisites')
class PodcastUploadAdmin(admin.ModelAdmin):
    list_display = ('podcasttitle','podcastcategory','podcastspeaker','podcastdesc','organisationofspeaker','podcastdateadded','podcastthumbnail','podcastaudiofile')
class ExperienceUploadAdmin(admin.ModelAdmin):
    list_display = ('studentname','studentphoto','branch','passoutyear','companyplaced','experience')
class JobUploadAdmin(admin.ModelAdmin):
    list_display = ('companyname','post','vacantseats','jobdesc','location','education')
class RegisterCourseAdmin(admin.ModelAdmin):
    list_display = ('coursename','registeredby','form_submitted')
admin.site.register(RegisterCourse,RegisterCourseAdmin)
admin.site.register(ExperienceUpload,ExperienceUploadAdmin)
admin.site.register(JobUpload,JobUploadAdmin)
admin.site.register(CourseUpload,CourseUploadAdmin)
admin.site.register(Question)
admin.site.register(Response)
admin.site.register(UserProfile)
admin.site.register(PodcastUpload,PodcastUploadAdmin)
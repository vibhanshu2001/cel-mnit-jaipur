from django.contrib import admin
from .models import CourseUpload, RegisterCourse, ExperienceUpload, Question, Response, JobUpload
# Register your models here.
class CourseUploadAdmin(admin.ModelAdmin):
    list_display = ('coursetitle','category','uploadedby','coursedesc','dateadded','thumbnailcourse','courselink')
class ExperienceUploadAdmin(admin.ModelAdmin):
    list_display = ('studentname','branch','passoutyear','companyplaced','experience')
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

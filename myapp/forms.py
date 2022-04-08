from django import forms
from django.contrib.auth.models import User
from .models import CourseUpload,Question, Response
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from .models import UserProfile,PodcastUpload,ExperienceUpload


class ExtendedUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    first_name = forms.CharField(max_length=30)
    last_name = forms.CharField(max_length=150)
    class Meta:
        model = User
        fields = ('username','email','first_name', 'last_name','password1','password2')
    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data['email']
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        if commit:
            user.save()
        return user
class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('usertype',)


class PodcastUploadForm(forms.ModelForm):
    class Meta:
        model = PodcastUpload
        fields = ('podcasttitle','podcastcategory','podcastspeaker','podcastdesc','organisationofspeaker','podcastthumbnail','podcastaudiofile')
        labels = {
            'podcasttitle': 'Podcast Title',
            'podcastcategory': 'Podcast Category',
            'podcastspeaker': 'Speaker',
            'podcastdesc': 'Description',
            'organisationofspeaker': 'Organisation of Speaker',
            'podcastthumbnail': 'Podcast Thumbnail',
            'podcastaudiofile': 'Upload Audio File'
        }
class ExperienceUploadForm(forms.ModelForm):
    class Meta:
        model = ExperienceUpload
        fields = ('studentphoto','studentname','branch','passoutyear','companyplaced','experience','studentcollege')
        labels = {
            'studentphoto': 'Upload Student Photo',
            'studentname': 'Student Name',
            'branch': 'Branch',
            'passoutyear': 'Passout Year',
            'companyplaced': 'Company Placed',
            'experience': 'Share your experience',
            'studentcollege': 'College Name'
        }
class CourseUploadForm(forms.ModelForm):
    class Meta:
        model = CourseUpload
        fields = ('coursetitle','category','coursedesc','thumbnailcourse','modulelink1','modulename1','modulelink2','modulename2','modulelink3','modulename3','modulelink4','modulename4','modulelink5','modulename5','modulelink6','modulename6','modulelink7','modulename7','modulelink8','modulename8','modulelink9','modulename9','modulelink10','modulename10','courseinstructorpicture','courseinstructor','aboutcourseinstructor','courseprerequisites')
        labels = {
            'coursetitle': 'Course Title',
            'category': 'Course Category',
            'coursedesc': 'Course Description',
            'modulelink1': 'Module 1 Link',
            'modulename1': 'Module 1 Name',
            'modulelink2': 'Module 2 Link',
            'modulename2': 'Module 2 Name',
            'modulelink3': 'Module 3 Link',
            'modulename3': 'Module 3 Name',
            'modulelink4': 'Module 4 Link',
            'modulename4': 'Module 4 Name',
            'modulelink5': 'Module 5 Link',
            'modulename5': 'Module 5 Name',
            'modulelink6': 'Module 6 Link',
            'modulename6': 'Module 6 Name',
            'modulelink7': 'Module 7 Link',
            'modulename7': 'Module 7 Name',
            'modulelink8': 'Module 8 Link',
            'modulename8': 'Module 8 Name',
            'modulelink9': 'Module 9 Link',
            'modulename9': 'Module 9 Name',
            'modulelink10': 'Module 10 Link',
            'modulename10': 'Module 10 Name',
            'thumbnailcourse': 'Upload Thumbnail',
            'courseinstructorpicture': 'Upload Course Instructor Picture',
            'courseinstructor': 'Course Instructor Name',
            'aboutcourseinstructor': 'About Course Instructor',
            'courseprerequisites': 'Course Prerequisites',
        }
class NewQuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = ['title', 'body']
        widgets = {
            'title': forms.TextInput(attrs={
                'autofocus': True,
            })
        }

class NewResponseForm(forms.ModelForm):
    class Meta:
        model = Response
        fields = ['body']

class NewReplyForm(forms.ModelForm):
    class Meta:
        model = Response
        fields = ['body']
        widgets = {
            'body': forms.Textarea(attrs={
                'rows': 2,
                'placeholder': 'What are your thoughts?'
            })
        }
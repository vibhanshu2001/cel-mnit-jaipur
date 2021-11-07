from django import forms
from django.contrib.auth.models import User
from .models import CourseUpload,Question, Response
from django.forms import ModelForm


class CourseForm(forms.ModelForm):
 class Meta:
  model = CourseUpload
  fields = ['coursetitle','coursedesc']
  labels = {'coursetitle':'Course Title', 'coursedesc': 'Course Description'}
  widgets = {
   'coursetitle':forms.TextInput(attrs={'class':'form-control'}),
   'coursedesc':forms.TextInput(attrs={'class':'form-control'}),
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
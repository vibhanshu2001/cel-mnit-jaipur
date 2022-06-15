from django.shortcuts import render,redirect
import requests,random
from django.http import HttpResponse
from django.contrib.auth import get_user_model
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import CourseUpload, RegisterCourse, ExperienceUpload, Question, Response, JobUpload, UserProfile,PodcastUpload
from django.views.generic import View
from .forms import NewQuestionForm, NewResponseForm, NewReplyForm, ExtendedUserCreationForm, UserProfileForm,PodcastUploadForm, CourseUploadForm, ExperienceUploadForm
from django.utils.decorators import method_decorator
from django.contrib.auth.forms import UserCreationForm

# Create your views here.
def index(request):
    jobdata = JobUpload.objects.last()
    questions = Question.objects.last()
    print(questions)
    data = CourseUpload.objects.all()
    if request.method == 'POST':
        register_course = RegisterCourse()
        register_course.coursename = request.POST['coursename']
        register_course.registeredby = request.user.username
        if not register_course.form_submitted:
            register_course.form_submitted = True
            register_course.save()
        else:
            print('already registered')
    return render(request, 'index.html',{'data':data,'jobdata':jobdata,'questions': questions})


# @login_required(login_url='handleLogin')
# def addcourse(request):
#     if request.method == 'POST':
#         course_upload = CourseUpload()
#         course_upload.coursetitle = request.POST['coursetitle']
#         course_upload.thumbnailcourse = request.FILES.get('thumbnailcourses')
#         course_upload.coursedesc = request.POST['coursedesc']
#         course_upload.courselink = request.POST['courselink']
#         course_upload.category = request.POST['category']
#         course_upload.uploadedby = request.user.username
#         course_upload.save()
        
#         return redirect('allcourses')
#     return render(request, 'addcourses.html')
@login_required(login_url='login')
def addcourse(request):
    if request.method == 'POST':
        form = CourseUploadForm(request.POST,request.FILES)
        if form.is_valid():
            new_record = form.save(commit=False)
            new_record.uploadedby = request.user.username
            new_record.save()
            return redirect('/allcourses')
    form = CourseUploadForm()
    return render(request,'addcourses.html',{'form':form})



@login_required(login_url='login')
def addpodcast(request):
    if request.method == 'POST':
        form = PodcastUploadForm(request.POST,request.FILES)
        if form.is_valid():
            new_record = form.save(commit=False)
            new_record.save()
            return redirect('/allpodcasts')
    form = PodcastUploadForm()
    return render(request,'addpodcasts.html',{'form':form})

def about(request):
    return render(request, 'about.html')
def results(request):
    return render(request, 'results.html')
@login_required(login_url='login')
def allusers(request):
    User = get_user_model()
    users = User.objects.all()
    return render(request, 'allusers.html',{'users':users})
@login_required(login_url='login')
def alljobs(request):
    jobdata = JobUpload.objects.all()
    return render(request, 'alljobs.html',{'jobdata':jobdata})
@login_required(login_url='login')
def addJob(request):
    if request.method == 'POST':
        job_upload = JobUpload()
        job_upload.companyname = request.POST['companyname']
        job_upload.post = request.POST['post']
        job_upload.vacantseats = request.POST['vacantseats']
        job_upload.jobdesc = request.POST['jobdesc']
        job_upload.location = request.POST['jobloc']
        job_upload.education = request.POST['education']
        job_upload.save()
        
        return redirect('/alljobs')
    return render(request, 'addjob.html')
@method_decorator(login_required, name='dispatch')
class CourseView(View):
 def get(self, request, pk):
  data = CourseUpload.objects.all()
  print(data)
  coursedetail = CourseUpload.objects.get(pk=pk)
  return render(request, 'coursedetail.html', {'coursedetail':coursedetail,'data':data})



@login_required(login_url='login')
def addexperience(request):
    if request.method == 'POST':
        form = ExperienceUploadForm(request.POST,request.FILES)
        if form.is_valid():
            new_record = form.save(commit=False)
            new_record.save()
            return redirect('/experience')
    form = ExperienceUploadForm()
    return render(request,'addexperience.html',{'form':form})

def experience(request):
    data = ExperienceUpload.objects.all()
    return render(request, 'ptcellexperience.html',{'data':data})

def allcourses(request):
    allcoursedata = CourseUpload.objects.all()
    return render(request, 'allcourses.html',{'allcoursedata':allcoursedata})
@login_required(login_url='login')
def allpodcasts(request):
    allpodcastdata = PodcastUpload.objects.all()
    return render(request, 'allpodcasts.html',{'allpodcastdata':allpodcastdata})

def handleLogin(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user= authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('index')
        else:
            return redirect('login')

    return render(request, 'login.html')
def handleLogout(request):
    logout(request)
    return redirect('login')
def signUp(request):
    if request.method == 'POST':
        form = ExtendedUserCreationForm(request.POST)
        profile_form = UserProfileForm(request.POST)
        if form.is_valid() and profile_form.is_valid():
            user = form.save()
            profile = profile_form.save(commit=False)
            profile.user = user
            profile.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('index')
    else:
        form = ExtendedUserCreationForm()
        profile_form = UserProfileForm()
        print('not happering')
    context = {'form': form,'profile_form':profile_form}
    return render(request, 'signup.html',context)        





@method_decorator(login_required, name='dispatch')
class EditView(View):
  def get(self, request,id):
    courseUpload = CourseUpload.objects.get(id=id)
    fm = CourseUploadForm(instance=courseUpload)
    return render(request,'updatecourse.html',{'form':fm})
  
  def post(self, request,id):
    courseUpload = CourseUpload.objects.get(id=id)
    form = CourseUploadForm(request.POST,request.FILES,instance=courseUpload)
    if form.is_valid():
      form.save()
    else:
      print('Reached here')
    return redirect("/allcourses")
@method_decorator(login_required, name='dispatch')
class DeleteView(View):
  def post(self, request,id):
    if request.method == 'POST':
        CourseUpload.objects.filter(id=id).delete()
    return redirect('/allcourses')


#comment
@login_required(login_url='register')
def newQuestionPage(request):
    form = NewQuestionForm()

    if request.method == 'POST':
        try:
            form = NewQuestionForm(request.POST)
            if form.is_valid():
                question = form.save(commit=False)
                question.author = request.user
                question.save()
                return redirect('allquestions')
        except Exception as e:
            print(e)
            raise

    context = {'form': form}
    return render(request, 'askquestion.html', context)

def allquestions(request):
    questions = Question.objects.all().order_by('-created_at')
    context = {
        'questions': questions
    }
    return render(request, 'allquestions.html', context)

def questionPage(request, id):
    response_form = NewResponseForm()
    reply_form = NewReplyForm()

    if request.method == 'POST':
        try:
            response_form = NewResponseForm(request.POST)
            if response_form.is_valid():
                response = response_form.save(commit=False)
                response.user = request.user
                response.question = Question(id=id)
                response.save()
                return redirect('/question/'+str(id)+'#'+str(response.id))
        except Exception as e:
            print(e)
            raise

    question = Question.objects.get(id=id)
    context = {
        'question': question,
        'response_form': response_form,
        'reply_form': reply_form,
    }
    return render(request, 'question.html', context)


@login_required(login_url='register')
def replyPage(request):
    if request.method == 'POST':
        try:
            form = NewReplyForm(request.POST)
            if form.is_valid():
                question_id = request.POST.get('question')
                parent_id = request.POST.get('parent')
                reply = form.save(commit=False)
                reply.user = request.user
                reply.question = Question(id=question_id)
                reply.parent = Response(id=parent_id)
                reply.save()
                return redirect('/question/'+str(question_id)+'#'+str(reply.id))
        except Exception as e:
            print(e)
            raise

    return redirect('index')
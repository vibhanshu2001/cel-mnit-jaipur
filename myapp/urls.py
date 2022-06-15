from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from . import views
from django.conf.urls.static import static
from django.conf import settings
urlpatterns = [
    path('',views.index, name="index"),
    path('about/',views.about, name="about"),
    path('allcourses/',views.allcourses, name="allcourses"),
    path('allpodcasts/',views.allpodcasts, name="allpodcasts"),
    path('alljobs/',views.alljobs, name="alljobs"),
    path('allusers/',views.allusers, name="allusers"),
    path('course/<int:pk>',views.CourseView.as_view(), name="coursedetail"),
    path('addcourse/',views.addcourse, name="addcourse"),
    path('addpodcast/',views.addpodcast, name="addpodcast"),
    path('addexperience/',views.addexperience, name="addexperience"),
    path('about/',views.about, name="about"),
    path('login/', views.handleLogin, name='login'),
    path('logout/', views.handleLogout, name='handleLogout'),
    path('signup/', views.signUp, name='signUp'),
    path('addjob/', views.addJob, name='addJob'),
    path('experience/', views.experience, name='experience'),
    path('updatecourse/<int:id>/', views.EditView.as_view(), name='update'),
    path('deletecourse/<int:id>/', views.DeleteView.as_view(), name='deletecourse'),
    path('allquestions/', views.allquestions, name='allquestions'),
    path('new-question', views.newQuestionPage, name='new-question'),
    path('question/<int:id>', views.questionPage, name='question'),
    path('reply', views.replyPage, name='reply'),
    path('results/',views.results, name="results"),
]
# urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

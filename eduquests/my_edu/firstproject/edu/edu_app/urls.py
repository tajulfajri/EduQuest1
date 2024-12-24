from django.urls import path, include
from . import views
from .views import  set_payment_session , check_session

app_name = "edu_app"

urlpatterns = [
    path('', views.home, name='home'),
    path('ourteam', views.ourteam, name='ourteam'),
    path('course', views.course, name='course'),
    path('login', views.login, name='login'),  
    path('signup', views.signup, name='signup'),
    path('dashboard', views.dashboard, name='dashboard'),
    path('logout', views.logout_view, name='logout'),
    path('class1', views.class1, name='class1'), 
    path('class2', views.class2, name='class2'), 
    path('class3', views.class3, name='class3'), 
    path('class4', views.class4, name='class4'), 
    path('class5', views.class5, name='class5'), 
    path('class6', views.class6, name='class6'), 
    path('belajarmenyenangkan', views.belajarmenyenangkan, name='belajarmenyenangkan'), 
    path('minatbakat', views.minatbakat, name='minatbakat'), 
    path('manajemenwaktu', views.manajemenwaktu, name='manajemenwaktu'),
    path('Inggrismudah', views.Inggrismudah, name='Inggrismudah'),
    path('materimodul1', views.materimodul1, name='materimodul1'),
    path('materimodul1class3', views.materimodul1class3, name='materimodul1class3'),
    path('Quizmodul1', views.Quizmodul1, name='Quizmodul1'), 
    path('quizmodul1class4', views.quizmodul1class4, name='quizmodul1class4'),
    path('modul1class6', views.modul1class6, name='modul1class6'),
    path('quizmodul1class6', views.quizmodul1class6, name='quizmodul1class6'),
    path('quizresult', views.quizresult, name='quizresult'),
    path('profil', views.profil, name='profil'),
    path('detail', views.detail, name='detail'),
    path('materimodul2', views.materimodul2, name='materimodul2'),
    path('materimodul3', views.materimodul3, name='materimodul3'),
    path('materimodul1class4', views.materimodul1class4, name='materimodul1class4'),
    path('Quizclass3', views.Quizclass3, name='Quizclass3'),
    path('courses', views.courses, name='courses'),
    path('kosakata', views.kosakata, name='kosakata'),
    path('leaderboard', views.leaderboard, name='leaderboard'),
    path('hasilquiz', views.hasilquiz, name='hasilquiz'),
    path('progressbelajar', views.progressbelajar, name='progressbelajar'),
    path('pembayaran', views.pembayaran, name='pembayaran'),
    path('check_payment_status/', views.check_payment_status, name='check_payment_status'),
    path('set-session/', set_payment_session, name='set_payment_session'),
    path('check-session/', check_session, name='check_session'),
   
]

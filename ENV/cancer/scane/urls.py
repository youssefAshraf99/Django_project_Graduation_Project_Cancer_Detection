from django.urls import path
from django.conf.urls import include
from django.urls import re_path
from . import views



urlpatterns=[

    path('',views.index,name='index'),
    path('about/',views.about,name='about'),
    path('contact/',views.contact,name='contact'),
    path('blogs/',views.blog,name='blog'),
    path('blog-details/',views.blog_details,name='blog-details'),
    path('doctors/',views.doctors,name='doctors'),
    path('about_new1/',views.about_News1,name='about_new1'),
    path('processing/',views.processing,name='processing'),
    path('translator/',views.HomeView.as_view(), name='form1'),
    path('transcriber/',views.HomeView2.as_view(), name='form2'),
    path('GC/',views.HomeView3.as_view(), name='form3'),
    path('motify/',views.HomeView4.as_view(), name='form4'),
    path('dnadis/',views.HomeView5.as_view(), name='form5'),
    path('Radiology_Diagnostics', views.Radiology_Diagnostics,name='Radiology_Diagnostics'),
    path('Radiology_result', views.show_res, name='show_res'),
    path('home/', views.home, name='home'),
    path('home/<str:room>/', views.room, name='room2'),
    path('home/checkview', views.checkview, name='checkview2'),
    path('home/send', views.send, name='send2'),
    path('home/getMessages/<str:room>/', views.getMessages, name='getMessages2'),
    path('<str:room>/', views.room, name='room'),
    path('checkview', views.checkview, name='checkview'),
    path('send', views.send, name='send'),
    path('getMessages/<str:room>/', views.getMessages, name='getMessages'),
    path('login', views.Login, name ='login'),
    path('registers', views.register, name ='register'),





    
    
 


    



    
    
]

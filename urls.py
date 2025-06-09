from . import views
import hipaa.urls
from django.urls import path,include
urlpatterns = [path('training/',views.training,name='training'),
               path('training/quiz/',views.quiz,name='quiz'),
               path('',views.homepage,name='homepage'),
               path('login/', views.login, name='login'),
               path('training/section2',views.section2,name='section2'),
               path('training/section3',views.section3,name='section3'),
               path('training/section4',views.section4,name='section4'),
               path('training/section5',views.section5,name='section5'),
               path('certificate',views.certificate,name='certificate'),]


"""
URL configuration for DjangoP1 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from DjangoP1 import views

#for media upload 
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", views.homepage),
    path("about-us/", views.aboutUs),
    path("facilities/", views.facilities),
    path("career/", views.career),
    path("gallery/", views.gallery),
    path("quiz-competition/", views.quiz),
    path("admission-enquiry/", views.admission),
    path("contactus/", views.contactus),
    path("calculate/", views.calculate)
    # path("course/", views.course),
    # path("course/<int:courseid>", views.courseDetails),
    # path("course/<str:courseid>", views.courseDetails),
    # path("course/<slug:courseid>", views.courseDetails),
    # path("course/<courseid>", views.courseDetails),
    
]

if settings.DEBUG:
    urlpatterns+=static(settings.MEDIA_URL, document_root= settings.MEDIA_ROOT)

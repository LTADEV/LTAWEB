import contextlib
from django.http import HttpResponse, HttpResponseRedirect

from django.shortcuts import render

from .forms import usersForm

#career data model
from career.models import Career

#gallery data model
from gallery.models import Gallery

#contact us form save
from contactenquiry.models import contactEnquiry

from admissionenquiry.models import admissionEnquiry

def homepage(request):
    # data={
    #     'title':"HomePage",
    #     'header':"Shovan's Homepage",
    #     'number':[10,20,30,40,50],
    #     'courselist':["Python","Java","PHP"],
    #     'studentdata':[
    #         {'name':"choc",'mobile':"78678767"},
    #         {'name':"tara",'mobile':"78678767"}
    #     ]
    # }
    data={}
    return render(request,"Frontend/index.html",data)

def aboutUs(request):
    return render(request,"Frontend/aboutus.html")

def facilities(request):
    return render(request,"Frontend/facilities.html")

def career(request):
    careerData= Career.objects.all()
    data ={'careerData':careerData}
    return render(request,"Frontend/career.html",data)

def gallery(request):
    galleryData= Gallery.objects.all()
    data ={'galleryData':galleryData}
    return render(request,"Frontend/gallery.html", data)

def quiz(request):
    return render(request,"Frontend/quiz.html")

def contactus(request):
    message=''
    fm =usersForm()
    data= {
        'form':fm,
        'message':message
    }
    with contextlib.suppress(Exception):
        name=request.POST['name']
        phone=request.POST['phone']
        email=request.POST['email']
        message=request.POST['message']
        
        en= contactEnquiry(name=name,phone=phone,email=email,message=message)
        en.save()
        
        if name != "" :
            message="Thank You , We will getback to you soon"
            data= {

                'message':message
            }
    return render(request,"Frontend/contactus.html",data)
def admission(request):
    data= {

                'message':'1'
            } 
    
    if request.method =="POST":
        name= request.POST.get('first_name') + request.POST.get('last_name')
        email= request.POST.get('email')
        phone= request.POST.get('phone')
        standard= request.POST.get('class')
        location= request.POST.get('location')
        message=request.POST.get('message')
        
        en=admissionEnquiry(name=name,phone=phone,email=email,standard=standard,location=location,message=message)
        en.save()
        message="Thank You , We will getback to you soon"
        data= {

                'message':message
            } 
        
     
    return render(request,"Frontend/admission-enquiry.html",data)

def calculate(request):
    return render(request,"Frontend/calculate.html")






# dynamic route

# def course(request):
#     return HttpResponse("welcome to shovans course")

# def courseDetails(request, courseid ):
#     return HttpResponse(courseid)
from django.http import HttpResponse
import datetime
from django.shortcuts import render


def home(request):
    date=datetime.datetime.now()
    isActive=True
    name="sumantech"
    list_of_program=[
        'WAP to check even or odd',
        'WAP to check prime number',
        'WAP to print all prime numbers from 1 to 100',
        'WAP to print pascals triangle'
        
        
    ]
    student={
        'student_name':"Rahuld",
        'student_college':"xyz",
        'student_city':"ktm"
    }
    
   
    #return HttpResponse("<h1>Hello this is index page </h1> "+str(date))
    data={
        'date':date,
        'isActive':isActive,
        'name':name,
        'list_of_program':list_of_program,
        'student_data':student
    }
    return render(request,"home.html",{})

def about(request):
    #return HttpResponse("<h1>This is about page</h>")
    return render(request,"about.html",{})

def services(request):
    #return HttpResponse("<h1>This is about services  page</h>")
    return render(request,"services.html",{})
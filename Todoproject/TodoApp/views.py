from django.shortcuts import render
from .models import Movie
# Create your views here.

def Home(req):
    movies=Movie.objects.all()
    return render(req,'index.html',{'movies':movies})
    
def registerUser(req):
    if req.method=='POST':
        fname=req.POST.get("fname","")
        lname=req.POST.get("lname","")
        email=req.POST.get("email","")
        username=req.POST.get("username","")
        password=req.POST.get("password","")
        cpassword=req.POST.get("cpassword","")
        print(fname,lname,email,username,password,cpassword)
    return render(req,'registeruser.html')    
if password==cpassword:
    if user.objects.filter

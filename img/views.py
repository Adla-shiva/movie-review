from django.shortcuts import render, redirect,get_object_or_404
from django.http import HttpResponse
from .models import pr,adminlg
from django.utils import timezone
import os


def index(request):
    post=pr.objects.all()
    return render(request, 'audiance.html',{'post':post})

def update(request,pk):
    username= request.session.get('username', 'NONE')
    password=request.session.get('password','NONE')
    if(username!="NONE" and password!="NONE"):
        prod= pr.objects.get(id=pk)
        if request.method == 'POST':
            if len(request.FILES)!= 0:
                if len(prod.image) > 0:
                    os.remove(prod.image.path)
                prod.image = request.FILES['edited_image']
            prod.title=request.POST['edited_title']
            # prod.image = request.FILES.get('edited_image')
            prod.description = request.POST['edited_description']
            prod.rating=request.POST['edited_rating']
            prod.date=request.POST['edited_release-date']
            prod.genre=request.POST['edited_genre']
            
        
            prod.save()
            return redirect('/fetching')
        
        return render(request, 'update.html', {'prod': prod})
    else:
        return redirect('/adminlog')

def delete(request,pk):
    username= request.session.get('username', 'NONE')
    password=request.session.get('password','NONE')
    if(username!="NONE" and password!="NONE"):
        prod = pr.objects.get(id=pk)
        if len(prod.image) > 0:
            os.remove(prod.image.path)
        prod.delete()
        return redirect('/fetching')
    else:
        return redirect('/adminlog')
   

def create(request):
    username= request.session.get('username', 'NONE')
    password=request.session.get('password','NONE')
    if(username!="NONE" and password!="NONE"):
        if request.method == 'POST':
            prod=pr()
            prod.title=request.POST['title']
            # prod.image = request.FILES.get('image')
            prod.description = request.POST['description']
            prod.rating=request.POST['rating']
            prod.date=request.POST['release-date']
            prod.genre=request.POST['genre']
            if len(request.FILES) != 0:
                prod.image = request.FILES['image']
            prod.save()
            # pr_instance=pr.objects.create(title=title,image=image,description=description,rating=rating,date=date,genre=genre)
            # pr_instance.save()
            return redirect('/fetching')
            
        return render(request, 'insert.html')
    else:
        return redirect('/adminlog')
def adminlog(request):
    post=pr.objects.all()
    if(request.method=="POST"):
        username=request.POST["username"]
        password=request.POST["password"]
        # x=adminlg.objects.get(username=username,password=password)
        condition={'username':username,'password':password}
        x=adminlg.objects.filter(**condition).exists()
        print(x,type(x),"before")
        if(x):
            request.session['username']=username
            request.session['password']=password
            return render(request,'fetching.html',{'post':post})
        else:
            return render(request,'adminlogin.html',{'error':"invalid credentials"})
    else:
        return render(request,'adminlogin.html')
        
        
def fetch(request):
    username= request.session.get('username', 'NONE')
    password=request.session.get('password','NONE')
    if(username!="NONE" and password!="NONE"):
        post=pr.objects.all()
        return render(request, 'fetching.html',{'post':post})
    else:
        return redirect('/adminlog')
    
def logout(request):
    request.session['username']="NONE"
    request.session['password']="NONE"
    return redirect('/adminlog')

def searchadmin(request):
    if(request.method=="POST"):
        pattern=request.POST["searchmovie"]
        username= request.session.get('username', 'NONE')
        password=request.session.get('password','NONE')
        if(username!="NONE" and password!="NONE"):
            if(pattern!=""):
                posts=pr.objects.filter(title__icontains=pattern)
                return render(request, 'fetching.html',{'post':posts})
            else:
                return redirect("/fetching")
        else:
            return redirect('/adminlog')
    else:
        return redirect("/fetching")
        
def searchuser(request):
    if(request.method=="POST"):
        pattern=request.POST["searchmovies"]
        posts=pr.objects.filter(title__icontains=pattern)
        return render(request, 'audiance.html',{'post':posts})
    else:
        return redirect("/")
      
            
    
    
    
    

        
# def srt(request):
#     if request.method == 'POST':
#         name = request.POST['text_input']
#         img = request.FILES['file_input']

#         # Create a new instance of the pr model
#         pr_instance = pr(name=name, img=img)

#         # Save the instance to the database
#         pr_instance.save()
#         x=pr.objects.all()
#         # print(x)
#         # print(type(x))
#         # l=[]
#         # for i in x:
#         #     l.append(i.img)
#         #     print(i.id)
#         # return HttpResponse(f"<img src='{l[0].url}' alt='Uploaded Image'>")
#         # return HttpResponse("successful")
#         return render(request,'in.html',{'x': x})
#     else:
#         return HttpResponse("unsuccessful")

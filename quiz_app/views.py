from django.shortcuts import render,redirect
from django.http import JsonResponse,HttpResponse
from django import forms
import random
from django.contrib.auth.hashers import check_password
from .forms import userregistration,question_form
from .models import questions,options
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
def home(request):
    return render(request,"home.html")
def register(request):
    if request.method=='POST':
      form=userregistration(request.POST)
      if form.is_valid():
        p=form.cleaned_data['password1']
        cp=form.cleaned_data['password2']
        if cp==p:
         user=User.objects.create_user(username=form.cleaned_data['username'],email=form.cleaned_data['email'],password=form.cleaned_data['password1'])
         
         return redirect('login')
    else:
       form=userregistration()
    return render(request,'register.html',{"f":form})
def user(request):
   name=request.user
   return render(request,'login.html',{'name':name})
@login_required
def ques(request):
     if request.method=="POST":
      score=0
      qu=list(request.POST.items())
      
      for q,a in qu:
        if q=='csrfmiddlewaretoken':
           continue
        q=questions.objects.get(id=int(q))
        c=q.options.get(option=a).is_true
        if c:
           score+=1
      return render(request,'score_board.html',{'user':request.user,'score':score})
     qu=questions.objects.all()
     arr=random.sample(list(qu),min(len(qu),10))
     qu=[]
     
     for i in arr:
        qu.append({"q":i,'ans':list(i.options.values_list('option',flat=True))})
     
     return render(request,'quiz.html',{"qu":qu})
@staff_member_required
def add(request):
    if request.method=="POST":
        form=question_form(request.POST)
        if form.is_valid():
            question=form.cleaned_data['question']
            question=questions.objects.create(question=question)
            o=[]
            o.append(form.cleaned_data['option1'])
            o.append(form.cleaned_data['option2'])
            o.append(form.cleaned_data['option3'])
            o.append(form.cleaned_data['option4'])
            co=int(form.cleaned_data['correct_option'])-1
            for i in o:
               if i==o[co]:
                options.objects.create(question=question,option=i,is_true=True)
               else:
                options.objects.create(question=question,option=i,is_true=False)

            return render(request,"home.html")   
    else:
        form=question_form()
    return render(request,"loginform.html",{"form":form})
    
def change(request):
   e=""
   class update(forms.Form):
    new_password=forms.CharField(max_length=50,widget=forms.PasswordInput)
    confirm_password=forms.CharField(max_length=50,widget=forms.PasswordInput)
   if request.method=='POST':
      form=update(request.POST)
      if form.is_valid():
         np=form.cleaned_data['new_password']
         cp=form.cleaned_data['confirm_password']
         p=User.objects.get(username=request.user)
         if cp==np and not check_password(cp,p.password):
          p.set_password(np)
          p.save()
          return redirect('login')
         elif cp!=np:
            e="password didn't match"
         else:
           e="same as last password"
   else:
         form=update()
   return render(request,'reset.html',{'form':form,'e':e})

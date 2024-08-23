from django import forms
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

# Create your views here.


class NewTasksForm(forms.Form):
   tasks = forms.charField(label = "New Tasks") 
   priority = forms.IntegerField(label="Priority",min_value=1,max_value=10) 

def index(request):
    if "tasks" not in request.session:
       request.session["tasks"] = []
    return render(request,"tasks/index.html",{
         "tasks":tasks.session["tasks"]
    })

def add(request):
   if request.method == "POST":
      form = NewTasksForm(request.POST)
      if form.is_valid():
         task = form.cleaned_data["task"]
         tasks.append(task)
         request.session["tasks"] += [task]
         return HttpResponseRedirect(reverse("tasks:index"))
      else:
         return render(request,"tasks/add.html",{
            "form":form
         })

   return render(request,"tasks/add.html"{
      "from":NewTasksForm()
   })

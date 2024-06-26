from django.shortcuts import render, HttpResponseRedirect
from .forms import StudentRegistration,ResumeForm
from .models import User,Resume
from django.views import View

# Create your views here.

# this function will add new item and show all items
def add_show(request):
    if request.method == 'POST':
        fm = StudentRegistration(request.POST)
        if fm.is_valid():
         nm = fm.cleaned_data['name']
         em = fm.cleaned_data['email'] 
         pw = fm.cleaned_data['password']
         reg = User(name=nm, email=em, password=pw)
         reg.save()  
         fm = StudentRegistration()
    else:
         fm = StudentRegistration()
    stud = User.objects.all()    
    return render(request, 'enroll/addandshow.html',{'form':fm, 'stu':stud})        

#this function will Update/Edit
def update_data(request, id):
    if request.method == 'POST':
        pi = User.objects.get(pk=id)
        fm = StudentRegistration(request.POST, instance=pi)
        if fm.is_valid():
            fm.save()
    else:
        pi = User.objects.get(pk=id)
        fm = StudentRegistration(instance=pi)
    return render(request, 'enroll/updatestudent.html', {'form':fm})    

# this function will delete items
def delete_data(request,id):
    if request.method == 'POST':
        pi = User.objects.get(pk=id)
        pi.delete()
        return HttpResponseRedirect('/')

class HomeView(View):
 def get(self, request):
  form = ResumeForm()
  candidates = Resume.objects.all()
  return render(request, 'enroll/home.html', { 'candidates':candidates, 'form':form})

 def post(self, request):
  form = ResumeForm(request.POST, request.FILES)
  if form.is_valid():
   form.save()
   return render(request, 'enroll/home.html', {'form':form})

class CandidateView(View):
 def get(self, request, pk):
  candidate = Resume.objects.get(pk=pk)
  return render(request, 'enroll/candidate.html', {'candidate':candidate})
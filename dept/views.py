from http.client import HTTPResponse
from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from .models import Emf, Faculty
from django.views.generic import CreateView
from django.contrib.auth import authenticate, login, logout

from .forms import *
from .models import Faculty
from django.contrib import messages
from django.coe.mail import send_mails

# Create your views here.
def home(request):
    return render(request, "authentication/base.html")
    
def enterc(request):
    return render(request, "authentication/enterc.html")

def add_faculty(request):
    submitted = False
    if request.method=="POST":
        form = FacultyForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/add_faculty?submitted=True')
    else:
        form = FacultyForm
        if 'submitted' in request.GET:
            submitted = True
    return render(request,"authentication/adding/add_faculty.html",{'form':form, 'submitted':submitted})

# def add_committee(request):
#     submitted = False
#     if request.method=="POST":
#         form =committeeForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return HttpResponseRedirect('/add_committee?submitted=True')
#     else:
#         form = committeeForm
#         if 'submitted' in request.GET:
#             submitted=True
#     return render(request,'authentication/loginc.html',{'form': form,'submitted':submitted})

def all_faculty(request):
    faculty_list = Faculty.objects.all()
    return render(request, 'authentication/faculty_list.html',{'faculty_list':faculty_list})

def sem_list(request):
    return render(request,'authentication/sem/sem_list.html')

def sem_listc(request):
    return render(request,'authentication/sem/sem_listc.html')

def subject6_list(request):
    return render(request, 'authentication/sem/subject6.html')
    


def subject6c_list(request):
    return render(request, 'authentication/sem/subject6c.html')       
    
def add_emf(request):
    submitted1 = False
    if request.method == "POST":
        form = EmfForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            send_mail(
                        'Subject here',
                        'Here is the message.',
                        'from@example.com',
                        ['to@example.com'],
                        fail_silently=False,
                    )
            return HttpResponseRedirect('/add_emf?submitted1=True')
    else:
        form = EmfForm
        if 'submitted1' in request.GET:
            submitted1 = True
    return render(request, 'authentication/adding/add_emf.html',{'form':form,'submitted1':submitted1})

# def emf(request):
#     submitted = False
#     if request.method == "POST":
#         form = emfdisplayForm(request.POST, request.FILES)
#         if form.is_valid():
#             form.save()
#             return HttpResponseRedirect('/emf?submitted=True')
#     else:
#         form = emfdisplayForm
#         if 'sunmitted' in request.GET:
#             submitted = True
#     return render(request, 'authentication/emf_disp.html',{'form':form, 'submitted':submitted})

# def emf(request):
#     data = Emf.objects.all()
#     context = {
#         'data': data
#     }
#     return render(request,'authentication/emf_disp.html',context)

        
    
def add_cn(request):
    submitted2 = False
    if request.method == "POST":
        form = cnForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/add_cn?submitted2=True')
    else:
        form = cnForm
        if 'submitted2' in request.GET:
            submitted2 = True
    return render(request, 'authentication/adding/add_cn.html',{'form':form,'submitted2':submitted2})

        
    
def add_ml(request):
    submitted3 = False
    if request.method == "POST":
        form = mlForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/add_ml?submitted3=True')
    else:
        form = mlForm
        if 'submitted3' in request.GET:
            submitted3 = True
    return render(request, 'authentication/adding/add_ml.html',{'form':form,'submitted3':submitted3})

        
    
def add_ws(request):
    submitted4 = False
    if request.method == "POST":
        form = wsForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/add_ws?submitted4=True')
    else:
        form = wsForm
        if 'submitted4' in request.GET:
            submitted4 = True
    return render(request, 'authentication/adding/add_ws.html',{'form':form,'submitted4':submitted4})

        
    
def add_iot(request):
    submitted5 = False
    if request.method == "POST":
        form = iotForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/add_iot?submitted5=True')
    else:
        form = iotForm
        if 'submitted5' in request.GET:
            submitted5 = True
    return render(request, 'authentication/adding/add_iot.html',{'form':form,'submitted5':submitted5})

def emfd(request):
    if request.method == "POST":
        form = EmfForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/done')
    else:
        form = EmfForm
    return render(request,'authentication/display/emf_disp.html',{'form':form})

def cnd(request):
    if request.method == "POST":
        form = cnForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/done')
    else:
        form = EmfForm
    return render(request,'authentication/display/cn_disp.html',{'form':form})

def wsd(request):
    if request.method == "POST":
        form = wsForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/done')
    else:
        form = wsForm
    return render(request,'authentication/display/ws_disp.html',{'form':form})

def mld(request):
    if request.method == "POST":
        form = mlForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/done')
    else:
        form = mlForm
    return render(request,'authentication/display/ml_disp.html',{'form':form})

def iotd(request):
    if request.method == "POST":
        form = iotForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/done')
    else:
        form = iotForm
    return render(request,'authentication/display/iot_disp.html',{'form':form})



def emfd(request):
    test_list1 = Emf.objects.all()
    return render(request, 'authentication/display/emf_disp.html', {'test_list1':test_list1})

def iotd(request):
    test_list2 = iot.objects.all()
    return render(request, 'authentication/display/iot_disp.html', {'test_list2':test_list2})

def wsd(request):
    test_list3 = ws.objects.all()
    return render(request, 'authentication/display/ws_disp.html', {'test_list3':test_list3})

def mld(request):
    test_list4 = ml.objects.all()
    return render(request, 'authentication/display/ml_disp.html', {'test_list4':test_list4})

def cnd(request):
    test_list5 = cn.objects.all()
    return render(request, 'authentication/display/cn_disp.html', {'test_list5':test_list5})

def commentemf(request):
    submitted1 = False
    if request.method=="POST":
        form = emfdisplayForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request,'authentication/sem/sem_listc.html')
    else:
        form = emfdisplayForm
        if 'submitted1' in request.GET:
            submitted1=True
    return render(request, 'authentication/ccomment/commentemf.html',{'form':form,'submitted1':submitted1})

def commentiot(request):
    submitted2 = False
    if request.method=="POST":
        form = iotdisplayForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request,'authentication/sem/sem_listc.html')
    else:
        form = iotdisplayForm
        if 'submitted2' in request.GET:
            submitted2=True
    return render(request, 'authentication/ccomment/commentiot.html',{'form':form,'submitted2':submitted2})

def commentws(request):
    submitted3 = False
    if request.method=="POST":
        form = wsdisplayForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request,'authentication/sem/sem_listc.html')
    else:
        form = wsdisplayForm
        if 'submitted3' in request.GET:
            submitted3=True
    return render(request, 'authentication/ccomment/commentws.html',{'form':form,'submitted3':submitted3})

def commentml(request):
    submitted4 = False
    if request.method=="POST":
        form = mldisplayForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request,'authentication/sem/sem_listc.html')
    else:
        form = mldisplayForm
        if 'submitted4' in request.GET:
            submitted4=True
    return render(request, 'authentication/ccomment/commentml.html',{'form':form,'submitted4':submitted4})

def commentcn(request):
    submitted5 = False
    if request.method=="POST":
        form = cndisplayForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request,'authentication/sem/sem_listc.html')
    else:
        form = cndisplayForm
        if 'submitted5' in request.GET:
            submitted5=True
    return render(request, 'authentication/ccomment/commentcn.html',{'form':form,'submitted5':submitted5})

def comment_dis_emf(request):
    list1 = emfdisplay.objects.all()
    return render(request, 'authentication/comdis/comment_dis_emf.html',{'list1':list1})

def comment_dis_iot(request):
    list2 = iotdisplay.objects.all()
    return render(request, 'authentication/comdis/comment_dis_iot.html',{'list2':list2})

def comment_dis_ws(request):
    list3 = wsdisplay.objects.all()
    return render(request, 'authentication/comdis/comment_dis_ws.html',{'list3':list3})

def comment_dis_ml(request):
    list4 = mldisplay.objects.all()
    return render(request, 'authentication/comdis/comment_dis_ml.html',{'list4':list4})

def comment_dis_cn(request):
    list5 = cndisplay.objects.all()
    return render(request, 'authentication/comdis/comment_dis_cn.html',{'list5':list5})

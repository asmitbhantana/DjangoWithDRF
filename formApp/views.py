from django.shortcuts import render
from django.http import HttpResponse

from .forms import MyForms, FormsModelForm
# Create your views here.
def forms_home(request):
    if request.method == 'GET':
        return render(request, 'FormApp/forms.html')
    else: 
        print(request.POST)
        return HttpResponse("Form Submitted!")

def django_form(request):
    if request.method == 'GET':
        form = MyForms()
        return render(request, "FormApp/django_form.html", {"form":form})
    else:
        form = MyForms(request.POST)
        if form.is_valid():
            print(request.POST)
            return HttpResponse("Django Form Submitted")
        else:
            return HttpResponse("Something Wrong")

def django_model_form(request):
    if request.method == 'GET':
        form = FormsModelForm()
        return render(request, "FormApp/forms_model.html", {"form":form})
    else:
        form = FormsModelForm(request.POST)
        if form.is_valid():
            form.save()
            print(request.POST)
            return HttpResponse("Django Form Submitted")
        else:
            return render(request, "FormApp/forms_model.html", {"form":form})

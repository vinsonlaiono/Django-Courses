from django.shortcuts import render, redirect, HttpResponse
from .models import *

# Create your views here.
def index(request):
    courses = Course.objects.all()
    return render(request, "first_app/index.html", {'courses':courses})
def process(request):
    if request.method == "POST":
        name = request.POST['name']
        desc = request.POST['description']
        course = Course.objects.create(name = name, desc = desc)
        course.save()
        return redirect('/')
def remove(request, id):
    course = Course.objects.get(id=id)
    return render(request, 'first_app/remove.html', {'course':course})
def delete(request, id):
    del_user = Course.objects.get(id=id)
    del_user.delete()
    return redirect('/')
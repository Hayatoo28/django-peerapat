from django.shortcuts import render
from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

def members(request):
    template = loader.get_template('myfirst.html')
    return HttpResponse("Hello world!")


def profile(request):
    template = loader.get_template('profile.html')
    return HttpResponse("Welcome to profile page")

def school(request):
    template = loader.get_template('school.html')
    return HttpResponse("โรงเรียนจิตรลดาวิชาชีพ")

# Create your views here.
from django.http import HttpResponse
from django.contrib.auth import authenticate, login,logout
from course.models import *
import os
from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from google.oauth2 import id_token
from google.auth.transport import requests
from django.http import JsonResponse
from django.template import loader
from django.conf import settings
from django.contrib.auth.models import User
from . import models
from dotenv import load_dotenv

def homepage(request):
    template = loader.get_template('homepage.html')
    return HttpResponse(template.render())

def training(request):
    template = loader.get_template('training.php')
    return HttpResponse(template.render())

def quiz(request):
    template = loader.get_template('quiz.html')
    questions = Ques.objects.all()
    return HttpResponse(template.render())

def section2(request):
    template = loader.get_template('section2.php')
    return HttpResponse(template.render())

def section3(request):
    template = loader.get_template('section3.html')
    return HttpResponse(template.render())

def section4(request):
    template = loader.get_template('section4.html')
    return HttpResponse(template.render())

def section5(request):
    template = loader.get_template('section5.html')
    return HttpResponse(template.render())

def certificate(request):
    template = loader.get_template('certificate.html')
    return HttpResponse(template.render())
def statement(request):
    template = loader.get_template('statement.html')
    return HttpResponse(template.render())
def unauthorized(request):
    template = loader.get_template('unauthorized.html')
    return HttpResponse(template.render())

@csrf_exempt
def login(request):
    load_dotenv()
    print('requestattempt')
    token=request.POST.get('credential')
    try:
        print("login")
        user_data = id_token.verify_oauth2_token(
            token, requests.Request(), os.getenv("CLIENT_ID")
        )
        email = user_data['email']
        #save email as user id to database and attach score
        user,created = User.objects.get_or_create(email=email,defaults={'username':email})
        allowed = ValidUser.objects.values_list('email', flat=True)
        print(allowed)
        if email in allowed:
            return redirect('training')
        else:
            return redirect('unauthorized')
    except ValueError:
        return HttpResponse(status=403)
    
def getenvvar(request):
    load_dotenv()
    print('request')
    clientid=os.getenv("CLIENT_ID")
    return JsonResponse({'client_id': clientid})



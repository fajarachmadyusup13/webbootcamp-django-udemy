from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    return HttpResponse("<em>My Second App</em>")

def help(request):
    helpDict = {'help_insert' : 'HELP PAGE'}
    return render(request, 'AppTwo/help.html', context = helpDict)

def user(request):
    return HttpResponse("BOOOM")
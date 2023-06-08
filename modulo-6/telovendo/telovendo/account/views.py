from django.shortcuts import render

from django.contrib.auth.models import User
# Create your views here.
def index(request):
    
    users = User.objects.all()
    return render(request, 'account/index.html')

def pg2(request):
    users = User.objects.all()
    return render(request, 'account/pg2.html', { 'users':users})
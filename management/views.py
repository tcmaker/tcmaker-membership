from django.shortcuts import render, redirect
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect

@login_required
def index(request):
    context = {}
    return render(request, 'management/index.html', context)

@login_required
def signout(request):
    logout(request)
    return redirect('/')

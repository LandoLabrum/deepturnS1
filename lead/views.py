from django.shortcuts import render
# from django.contrib.auth.decorators import login_required
# from django.contrib import messages
# from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
# from django.contrib.auth.models import User
from django.http import HttpResponseRedirect

def FormOne(request):
    context = {}
    if request.method == 'POST':
        print(request.POST)
    if request.method == 'GET':
        print(request.GET)

    return render(request, 'lead/main.html', context)
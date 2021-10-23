from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.http import HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt
# from django.contrib.auth.decorators import login_required
# from django.contrib import messages
# from django.contrib.auth import authenticate, login, logout
# from django.contrib.auth.models import User

# from .models import form_one_model
# from lead.models import lead_model
# from .serializers import form_one_serializer

@csrf_exempt
def form_one_view(request):
    context = {}
    if request.method == 'POST':
        print(request.POST)
    if request.method == 'GET':
        print(request.GET)
    return render(request, 'home.html', context)
    # return JsonResponse(context)
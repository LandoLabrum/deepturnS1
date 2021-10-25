from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.http import HttpResponseRedirect
# from django.views.decorators.csrf import csrf_exempt
# from django.contrib.auth.decorators import login_required
# from django.contrib import messages
# from django.contrib.auth import authenticate, login, logout
# from django.contrib.auth.models import User
from datetime import datetime
import time
from .serializers import one_serializer, lead_serializer
from .models import one_question


def session_handler(request):
    context = {}
    session = request.session
    post = request.POST
    key = post['fid']
    type = post['type']
    if type == 'radio' or type == 'range':
        context[key] = post['value']
        session.__setitem__(key, context[key])
    elif type == 'checkbox' or type == 'Contact':
        val = ''
        context[key] = []
        for i in post:
            if i not in {'fid', 'type', 'csrfmiddlewaretoken', 'next'}:
                context[key].append(i)
        session.__setitem__(key, context[key])

    elif type == 'Submit':
        # print(f"POST: {post}")
        lead = {}
        format = "%b %d, %Y at %H:%M %p"
        date_str = f"{post['date']} at {post['time']}"
        print(f"date {date_str}")
        meeting = int(time.mktime(
            datetime.strptime(date_str, format).timetuple()))
        for i in post:
            if i not in {'fid', 'type', 'csrfmiddlewaretoken', 'next', 'time', 'date'}:
                lead.update({i: post[i]})
        serializer = lead_serializer(data=lead)
        if serializer.is_valid():
            serializer.save()
            print(f"VALID_LEAD: {serializer}")
            session.__setitem__("lead", post['email'])
            session.__setitem__("meeting", meeting)
            session.__setitem__("meeting_str", date_str)
            return True
        else:
            return serializer.errors


# @csrf_exempt


def one_view(request):
    next = None
    context = {}
    if request.method == 'GET':
        next = 'age_range'
    if request.method == 'POST':
        data = request.POST 
        next = data['next']
        session = session_handler(request)
    if next == 'meeting':
        context['type'] = 'Contact'
        context['dates']=['Oct 24, 2021', 'Oct 25, 2021', 'Oct 26, 2021']
        context['times']=['8:15 AM', '8:30 AM', '8:45 AM']
    elif next == 'submit':
        all_session = dict(request.session.items())
        # print(f"SESSION: \t {request.session.items()}")
        serializer = one_serializer(data=all_session)
        if serializer.is_valid():
            if session == True:
                serializer.save()
                print(f"VALID_FORM: {serializer}")
                context['meeting'] = request.POST
 
        else:
            context['errors']={}
            context['errors']['lead'] = session
            context['errors']['form'] = serializer.errors
            # print(f'errs141: \t {serializer.errors}')
            # print(f'errs142: \t {session}')
    else:
        context = list(one_question.objects.filter(fid=next).values())[0]
        context['choices'] = context['choices'].split(";")
    return render(request, 'form/index.html', context)

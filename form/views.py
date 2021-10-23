from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.http import HttpResponseRedirect
# from django.views.decorators.csrf import csrf_exempt
# from django.contrib.auth.decorators import login_required
# from django.contrib import messages
# from django.contrib.auth import authenticate, login, logout
# from django.contrib.auth.models import User

from .models import one, one_question
from lead.models import lead_model
from .serializers import one_serializer

def session_handler(request):
    context={}
    session=request.session
    post=request.POST
    key=post['field_id']
    type=post['type']
    if type == 'radio' or type == 'range':
        context[key]=post['value']
    elif type == 'checkbox' or type == 'Contact':
        val=''
        context[key]=[]
        print(f'post: {post}')
        for i in post:
            
            if i not in {'field_id', 'type', 'csrfmiddlewaretoken', 'next'}:
                context[key].append(i)
    # session.__setitem__(key, context[key])


# @csrf_exempt
def one_view(request):
    next=None
    context={}
    if request.method == 'GET':
        next='age_range'
    if request.method == 'POST':
        data=request.POST
        next=data['next']
    s=session_handler(request)
    if next == 'contact':
        context['type']='Contact'

    elif next == 'submit':
        all_session=dict(request.session.items())
        print(f"SESSION: \t {request.session.items()}")
        serializer = one_serializer(data=all_session)
        if serializer.is_valid():
            print('VALID')
        else:
            print(serializer.errors)
    else:
        context = list(one_question.objects.filter(field_id=next).values())[0]
        context['choices']=context['choices'].split(";")
    return render(request, 'form/index.html', context)

       # print(f'POST DATA: \t {data}')
        # serializer = one_serializer(data=data)
        # if serializer.is_valid():
        #     print('valid')
        # else:
        #     print(f"errors: \t {serializer.errors}")
# print('\n ###### ALL SESSION ITEMS #######')        
# for key, value in request.session.items():
#     print('{} => {}'.format(key, value))
# print('###### ALL SESSION ITEMS END ####### \n')  
import json
from datetime import datetime
import time

from django.http import JsonResponse
from .serializers import F101Serializer, LeadSerializer
from .models import F101



def F101View(request):
    context = {}
    if request.method == 'POST':
        d = json.loads(request.body)['body']
        print(f'D \t \t {d}')
        dt_string = f"{d['appointment']['date']}T{d['appointment']['time']}"
        d['lead'] = d['appointment']['email']
        d['teachable'] = int(d['teachable'])
        d['appointment']['src'] = 'F101'
        print(d['appointment'])
        lSerializer = LeadSerializer(data=d['appointment'])

        
        if lSerializer.is_valid():
            lSerializer.save()
            context['lead']={
                "status":"success",
                'appointment': dt_string
                }

            format = "%Y-%m-%dT%H:%M"
            d['meeting'] = int(time.mktime(datetime.strptime(dt_string, format).timetuple()))
            # print(f"type: {type(d['appointment'])}, \t APPT: {d['appointment']}")
            fSerializer = F101Serializer(data=d) 
            if fSerializer.is_valid():
                fSerializer.save()
                context['form']={
                    "status":"success",
                    'appointment': dt_string
                    }
            else:
                print(f'ERRORS1: \t {fSerializer.errors}')
                context['form']={
                    "status":"error",
                    'appointment': dt_string,
                    'errors': fSerializer.errors
                }
        else:
            print(f'ERRORS: \t {lSerializer.errors}')
            context['lead']={
                "status":"error",
                'appointment': dt_string,
                'errors': lSerializer.errors
            }

        

    return JsonResponse(context)


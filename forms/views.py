import json
from datetime import datetime
import time

from django.http import JsonResponse
from .serializers import F101Serializer, LeadSerializer
from .models import F101
from lead.models import Lead


def F101View(request):
    context = {}
    if request.method == 'POST':
        d = json.loads(request.body)['body']
        dt_string = f"{d['appointment']['date']} at {d['appointment']['time']}"
        d['teachable'] = int(d['teachable'])
        d['appointment']['src'] = 'F101'
        lSerializer = LeadSerializer(data=d['appointment'])
        if lSerializer.is_valid():
            lSerializer.save()
            context['lead']={
                "status":"success",
                'appointment': dt_string
                }

            format = "%Y-%m-%d at %H:%M"
            d['meeting'] = int(time.mktime(datetime.strptime(dt_string, format).timetuple()))
            d['lead'] = d['appointment']['email']
            d.pop('appointment')
            fSerializer = F101Serializer(data=d) 
            if fSerializer.is_valid():
                fSerializer.save()
                context['form']={
                    "status":"success",
                    'appointment': dt_string
                    }
            else:
                context['form']={
                    "status":"error",
                    'appointment': dt_string,
                    'errors': fSerializer.errors
                }
        else:
            
            context['lead']={
                "status":"error",
                'appointment': dt_string,
                'errors': lSerializer.errors
            }
    return JsonResponse(context)


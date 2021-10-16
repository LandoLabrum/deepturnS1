import json
from datetime import datetime

from django.http import JsonResponse

from .models import Leads

def leads(request):
    context = {}
    if request.method == 'POST':
        d = json.loads(request.body)['body']
        dt_string = f"{d['appointment']['date']} {d['appointment']['time']}"
        format = "%Y-%m-%d %H:%M"
        dt_object = datetime.strptime(dt_string, format)
        context={
            "status":"success",
            'appointment': dt_string
            }
    return JsonResponse(context)


import json
from datetime import datetime

from django.http import JsonResponse

def lead(request):
    context = {}
    if request.method == 'POST':
        d = json.loads(request.body)['body']
        dt_string = f"{d['appointment']['date']} {d['appointment']['time']}"
        format = "%Y-%m-%d %H:%M"
        dt_object = datetime.strptime(dt_string, format)
        if True:
            context={
                "status":"success",
                'appointment': dt_string
                }
        else:
            context={
                "status":"error",
                'appointment': dt_string
            }
    return JsonResponse(context)


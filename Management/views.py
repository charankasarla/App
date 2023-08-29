import os
from django.conf import settings
from django.shortcuts import render
import json

# Create your views here.


managementjson = os.path.join(settings.MEDIA_ROOT,'management.json')
#print(managementjson)
def management(request):
    try:
        with open(managementjson) as f:
            data = json.load(f)
    except:
        data = {}
    jsondata =json.dumps(data)

    context = {"jsondata":jsondata}
    context.update(data)

    #print(context['zonestats'])


    #print(data)
    return render(request, 'management.html', context )
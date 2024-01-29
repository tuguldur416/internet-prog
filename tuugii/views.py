# timeservice/views.py
from django.http import JsonResponse
from datetime import datetime

def current_time(request):
    now = datetime.now()
    formatted_time = now.strftime("%Y-%m-%d %H:%M:%S")
    return JsonResponse({'current_time': formatted_time})


# Create your views here.

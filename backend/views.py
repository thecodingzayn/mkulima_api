# backend/views.py
from django.http import JsonResponse

def home(request):
    return JsonResponse({"message": "Mkulima API is live!"})

from django.shortcuts import render
from django.http import JsonResponse
import json


# Page view (HTML)
def api_form(request):
    return render(request, "api_form.html")


# API view (receives data)
def my_api(request):
    if request.method == "POST":
        data = json.loads(request.body)

        name = data.get("name")
        age = data.get("age")

        return JsonResponse({
            "message": f"Hello {name}, you are {age} years old!"
        })

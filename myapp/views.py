from django.shortcuts import render
from django.http import JsonResponse
from .models import User
import json
from django.views.decorators.csrf import csrf_exempt
import bcrypt

@csrf_exempt
def user(request):
    print("hey user")
    try:
        if request.method == 'POST':
            data = json.loads(request.body)
            useremail = data['useremail']
            password = data['password'].encode('utf-8')
            hashed_password = bcrypt.hashpw(password, bcrypt.gensalt()).decode('utf-8')
            user = User(useremail=useremail, password=hashed_password)
            user.save()
            return JsonResponse({"msg":"data inserted","status":"success"})
        else:
            return "hello"
    except Exception as e:
        import traceback
        traceback.print_exc()
        return JsonResponse({"status":"error","message":str(e)})

@csrf_exempt
def genre(request):
    print("hey user")
    try:
        if request.method == 'POST':
            data = json.loads(request.body)
            name = data['name']
            description = data['description']
            genra = genre(name=name, description = description)
            genre.save()
            return JsonResponse({"msg":"data inserted","status":"success"})
        else:
            return "hello"
    except Exception as e:
        import traceback
        traceback.print_exc()
        return JsonResponse({"status":"error","message":str(e)})
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
            print(useremail,password)
            # user.save()
            return JsonResponse({"msg":"data inserted","status":"success"})
        else:
            return "hello"
    except Exception as e:
        import traceback
        traceback.print_exc()
        return JsonResponse({"status":"error","message":str(e)})

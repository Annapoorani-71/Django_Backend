from django.contrib.auth import authenticate
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import User
import json

@csrf_exempt
def user_create(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        name = data.get('name', '')
        fname = data.get('fname', '')
        email = data.get('email', '')
        password = data.get('password', '')

        # Create a new user object
        new_user = User(name=name, fname=fname, email=email, password=password)
        new_user.save()

        return JsonResponse({'message': 'User created successfully!'})

    return JsonResponse({'error': 'POST request required'})


@csrf_exempt
def user_login(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        email = data.get('email', '')
        password = data.get('password', '')

        try:
            user = User.objects.get(email=email, password=password)
            return JsonResponse({'message': 'Login successful!', 'email': user.email})
        except User.DoesNotExist:
            return JsonResponse({'error': 'Invalid email or password'}, status=401)

    return JsonResponse({'error': 'POST request required'})

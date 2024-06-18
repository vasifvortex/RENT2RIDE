from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Cycle
import json
def read(request):
    cycles = Cycle.objects.all()
    data = [{'id': cycle.id, 'name': cycle.name, 'type': cycle.type, 'price': cycle.price, 'comment': cycle.comment, 'image': cycle.image.url if cycle.image else ''} for cycle in cycles]
    return JsonResponse(data, safe=False)
def read_single(request, cycle_id):
    try:
        cycle = Cycle.objects.get(id=cycle_id)
        data = {
            'id': cycle.id,
            'name': cycle.name,
            'type': cycle.type,
            'price': cycle.price,
            'comment': cycle.comment,
            'image': cycle.image.url if cycle.image else ''
        }
        return JsonResponse(data)
    except Cycle.DoesNotExist:
        return JsonResponse({'error': 'Cycle not found'}, status=404)
    
from django.views.decorators.csrf import csrf_exempt
import json

@csrf_exempt
def create(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            cycle = Cycle.objects.create(
                name=data['name'],
                type=data['type'],
                price=data['price'],
                comment=data['comment'],
                image=data['image']
            )
            return JsonResponse({'message': 'Cycle created successfully'}, status=201)
        except json.JSONDecodeError:
            return JsonResponse({'error': 'Invalid JSON'}, status=400)
        except KeyError as e:
            return JsonResponse({'error': f'Missing field: {e}'}, status=400)
    else:
        return JsonResponse({'error': 'Method not allowed'}, status=405)
    
@csrf_exempt
def update(request, cycle_id):
    try:
        cycle = Cycle.objects.get(id=cycle_id)
        if request.method == 'PUT':
            data = json.loads(request.body)
            cycle.name = data.get('name', cycle.name)
            cycle.type = data.get('type', cycle.type)
            cycle.price = data.get('price', cycle.price)
            cycle.comment = data.get('comment', cycle.comment)
            cycle.image = data.get('image', cycle.image)
            cycle.save()
            return JsonResponse({'message': 'Cycle updated successfully'})
        else:
            return JsonResponse({'error': 'Method not allowed'}, status=405)
    except Cycle.DoesNotExist:
        return JsonResponse({'error': 'Cycle not found'}, status=404)


def delete(request, cycle_id):
    try:
        cycle = Cycle.objects.get(id=cycle_id)
        cycle.delete()
        return JsonResponse({'message': 'Cycle deleted successfully'})
    except Cycle.DoesNotExist:
        return JsonResponse({'error': 'Cycle not found'}, status=404)
    

from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import login
from django.contrib import messages
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def register(request):
    if request.method == 'POST':
        name = request.POST['name']
        surname = request.POST['surname']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        repeat_password = request.POST['repeat_password']

        if password == repeat_password:
            if User.objects.filter(username=username).exists():
                messages.error(request, 'Username is already taken')
            elif User.objects.filter(email=email).exists():
                messages.error(request, 'Email is already registered')
            else:
                user = User.objects.create_user(
                    first_name=name,
                    last_name=surname,
                    username=username,
                    email=email,
                    password=password
                )
                user.save()
                login(request, user)
                messages.success(request, 'Registration successful')
                return redirect('index')
        else:
            messages.error(request, 'Passwords do not match')
    
    return render(request, 'registration.html')

from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

@login_required
def index(request):
    return render(request, 'index.html')

from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages

def login_view(request):
    if request.user.is_authenticated:
        return redirect('index')

    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('index')
            else:
                messages.error(request, 'Invalid username or password.')
        else:
            messages.error(request, 'Invalid username or password.')
    
    form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

def bikes(request):
    return render(request, 'bikes.html')


from django.shortcuts import render, get_object_or_404
from .models import Cycle

def bike(request, cycle_id):
    cycle = get_object_or_404(Cycle, id=cycle_id)
    return render(request, 'bike.html', {'bike': cycle})

from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.core.mail import send_mail
from django.conf import settings
from django.contrib import messages

def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        comment = request.POST.get('comment')

        # Send an email (this is a basic example, you might want to use a form and validate it)
        subject = f"New Contact from {name}"
        message = f"Name: {name}\nEmail: {email}\nPhone: {phone}\nComment: {comment}"
        from_email = settings.DEFAULT_FROM_EMAIL
        recipient_list = ['your-email@example.com']  # replace with your email address or a list of email addresses

        try:
            send_mail(subject, message, from_email, recipient_list)
            messages.success(request, 'Thank you for getting in touch! We will get back to you soon.')
        except Exception as e:
            messages.error(request, f"An error occurred: {e}")

        return redirect('contact')

    return render(request, 'contact.html')
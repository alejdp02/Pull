from django.shortcuts import render
from starbucks.models import Tabla
from django.shortcuts import get_object_or_404, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

# Create your views here.
@login_required
def home(request):
    food = Tabla.objects.all()
    context = {
        'food': food
    }
    return render(request, 'index.html', context)

@login_required
def incrementar_valor(request, item_id):
    item = Tabla.objects.get(id=item_id)
    print(item)
    item.pull += 1
    item.save()
    return redirect('home')

@login_required
def decrementar_valor(request, item_id):
    item = Tabla.objects.get(id=item_id)
    if item.pull > 0:
        item.pull -= 1
        item.save()
    return redirect('home')



def signin(request):
    if request.method == 'GET':
        print('utliza metodo get')
    else:
        user = authenticate(request, username=request.POST['username'], password=request.POST['password'])
        if user is None:
            return render(request, 'signin.html', {'error': 'Username or password is incorrect'})
        else:
            login(request, user)
            return redirect('home')
    return render(request, 'signin.html')

@login_required
def signout(request):
    logout(request)
    return redirect('signin')



def signup(request):
    if request.method == 'GET':
        print('metodo get')
        return render(request, 'signup.html')
    else:
        if request.POST['password'] == request.POST['password2']:
            try:
                print(request.POST)
                user = User.objects.create_user(username=request.POST['username'], password=request.POST['password'])
                print(user)
                user.save()
                login(request, user)
                return redirect('home')
            except:
                error_user = 'User already exists'
                return render(request, 'signup.html', {'error_user':error_user})
        else:
            error = 'The passwords do not match'
            return render(request, 'signup.html', {'error':error})

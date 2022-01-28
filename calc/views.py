from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User, auth
from django.shortcuts import render, redirect
from .models import Room
from .forms import RoomForm


# Create your views here.


def loginPage(request):
    page = 'login'
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        try:
            user = User.objects.get(username=username)
        except:
            messages.error(request, "User does not exists")

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'Username or password does not exists.')
    context = {'page': page}
    return render(request, 'login.html', context)


def logoutUser(request):
    logout(request)
    return redirect('home')


def registerUser(request):
    page = 'register'
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password1']
        password2 = request.POST['password2']

        if password == password2:
            if User.objects.filter(username=username).exists():
                messages.info(request, "The user already exists.")
                return redirect('register')
            else:
                user = User.objects.create_user(username=username, password=password)
                user.save()
                return redirect('login')
        else:
            messages.info(request, "The password is incorrect.")
            return redirect('register')
    context = {'page': page}
    return render(request, 'register.html', context)


def home(request):
    rooms = Room.objects.all()
    context = {'rooms': rooms}
    return render(request, 'home.html', context)


def room(request, pk):
    room_ = Room.objects.get(id=pk)
    context = {'room': room_}
    return render(request, 'room.html', context)


def createRoom(request):
    form = RoomForm()
    if request.method == 'POST':
        form = RoomForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    context = {'form': form}
    return render(request, 'room_form.html', context)


def updateRoom(request, pk):
    r = Room.objects.get(id=pk)
    fr = RoomForm(instance=r)

    context = {'form': fr}
    return render(request, 'room_form.html', context)


def deleteRoom(request, pk):
    r = Room.objects.get(id=pk)
    if request.method == 'POST':
        r.delete()
        return redirect('/')
    context = {'obj': r}
    return render(request, 'delete.html', context)

from django.contrib import messages
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, render, redirect

from .models import Profile

def profiles(request):
    profiles = Profile.objects.all()
    context = {'profiles': profiles}
    return render(request, 'users/profiles.html', context)


def userProfile(request, pk):
    profile = get_object_or_404(Profile, pk=pk)
    top_skills = profile.skill_set.exclude(description__exact="") #exclude the empty description
    other_skills = profile.skill_set.filter(description="")
    context = {'profile':profile, 'top_skills':top_skills, 'other_skills':other_skills}
    return render(request, 'users/user-profile.html', context)

def login_user(request):
    if request.user.is_authenticated:
        return redirect('profiles')
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        try:
            user = User.objects.get(username=username)
        except:
            messages.error(request, 'Username does not exist')
        
        '''
        authenticate() will query the database. If it finds the user that
        actually matches the username and password, then it's going to return
        back that user
        '''
        user = authenticate(request, username=username, password=password)

        if user is not None:
            '''
            login() will create a session for this user in the database (in Session Table)
            Then it's also going to get that session and it's going to add that into our
            browsers cookies.
            '''
            login(request, user)
            return redirect('profiles')
        else:
             messages.error(request, 'Username or Password is incorrect')

    return render(request, 'users/login_register.html')

def logout_user(request):
    logout(request)
    messages.error(request, 'User was logged out!')
    return redirect('login')
from django.shortcuts import render, redirect
from .models import *
from .forms import *
from django.http import HttpResponse
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from quizes.models import *



def sign_up(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST) 
        
        if form.is_valid():

            user = form.save()

            user.save()

            return redirect('sign_in')
    else:
        form = UserRegistrationForm()



    context = {
        'form': form,
    }

    return render(request, 'users/register.html', context)
       

@login_required
def sign_out(request):
    logout(request)
    return redirect('home')  




def sign_in(request):
    if request.method == 'GET':
        form = LoginForm()
        return render(request,'users/login.html', {'form': form})
    
    elif request.method == 'POST':
        form = LoginForm(request.POST)
        
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)

            if user:
                login(request, user)
                return redirect('home')
            
        context = {
            'form': form
            }
            
        return render(request, 'users/login.html', context)
            
@login_required
def edit_profile(request):
    if request.method == 'POST':
        user_form = UserEditForm(data=request.POST, instance=request.user)
        profile_form = ProfileEditForm(data=request.POST, files=request.FILES, instance=request.user.profile)

        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()

            return redirect('profile')

    else:
        user_form = UserEditForm(instance=request.user)
        profile_form = ProfileEditForm(instance=request.user.profile)

    context = {
        'user_form': user_form,
        'profile_form': profile_form
    }

    return render(request, 'users/settings.html', context)



@login_required
def user_daily_visits(request):
    user = request.user
    today = timezone.now().date()

    if not DailyVisit.objects.filter(user=user, date_visited=today).exists():
        

        DailyVisit.objects.create(user=user, date_visited=today)

    consecutive_days = DailyVisit.objects.filter(user=user, date_visited__lte=today).count()

    user_klass = Profile.objects.get(user=request.user) 
    subjects = Language.objects.filter(klass=user_klass.klass)

    leaderboard = TestResult.objects.order_by('-score')[:10]


    current_weekday = today.weekday()

    context = {
        'consecutive_days': consecutive_days,
        'current_weekday': current_weekday,
        'leaderboard': leaderboard,
        'subjects': subjects
    }

    return render(request, 'users/profile.html', context)
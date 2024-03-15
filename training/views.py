from django.http import HttpResponse
from quizes.models import *
from django.shortcuts import (
    redirect,
    render,
    get_list_or_404,
    get_object_or_404
)
from django.utils import timezone

from .models import *
from users.models import *
from django.contrib.auth.decorators import login_required


def faq(request):
    return render(request, 'training/faq.html')


def AtaAnalar(request):
    return render(request, 'training/ata_analar.html')


def Base(request):
    if request.user.is_authenticated:
        try:
            user = request.user
            today = timezone.now().date()

            if not DailyVisit.objects.filter(user=user, date_visited=today).exists():
                 
                DailyVisit.objects.create(user=user, date_visited=today)
                
            consecutive_days = DailyVisit.objects.filter(user=user, date_visited__lte=today).count()

            user_klass = Profile.objects.get(user=user)

            subjects = Language.objects.filter(klass=user_klass.klass)

            lessons = Lesson.objects.filter(klass=user_klass.klass)
                

            leaderboard = TestResult.objects.order_by('-score')[:10]

            context = {
                'subjects': subjects, 
                'leaderboard': leaderboard, 
                'lessons': lessons, 
                'consecutive_days': consecutive_days
            }

            return render(request, 'base.html', context)

        
        except Profile.DoesNotExist:
            return render(request, 'base.html')
    else:

        leaderboard = TestResult.objects.order_by('-score')[:10]

        lessons = Lesson.objects.all()

        languages = Language.objects.all()



    context = {
        'leaderboard': leaderboard,
        'lessons': lessons,
        'languages': languages
    }

    return render(request, 'base.html', context)


def LessonView(request, subject_slug):

    if request.user.is_authenticated:

        user = request.user
        today = timezone.now().date()

        if not DailyVisit.objects.filter(user=user, date_visited=today).exists():
                 
            DailyVisit.objects.create(user=user, date_visited=today)
        else:
            consecutive_days = DailyVisit.objects.filter(user=user, date_visited__lte=today).count()

        user_klass = Profile.objects.get(user=request.user) 

        subjects = Language.objects.filter(klass=user_klass.klass)

        leaderboard = TestResult.objects.order_by('-score')[:10]

        lesson_cat = Lesson.objects.filter(language__subject_slug = subject_slug)

            
        context = {
            'lesson_cat': lesson_cat,
            'subjects': subjects,
            'leaderboard': leaderboard,
            'consecutive_days': consecutive_days
        }
        
        return render(request, 'training/lesson.html', context)


    else:
        languages = Language.objects.all()
        


        lesson_cat = Lesson.objects.filter(language__subject_slug = subject_slug)
        leaderboard = TestResult.objects.order_by('-score')[:10]


        context = {
            'lesson_cat': lesson_cat,
            'leaderboard': leaderboard,
            'languages': languages
        }
        return render(request, 'training/lesson.html', context)
        


def LessonDetailView(request, slug):

    if request.user.is_authenticated:
        user = request.user
        today = timezone.now().date()

        if not DailyVisit.objects.filter(user=user, date_visited=today).exists():
                 
            DailyVisit.objects.create(user=user, date_visited=today)
        else:
            consecutive_days = DailyVisit.objects.filter(user=user, date_visited__lte=today).count()

        leaderboard = TestResult.objects.order_by('-score')[:10]

        user_klass = Profile.objects.get(user=request.user) 

        subjects = Language.objects.filter(klass=user_klass.klass)


        lesson = get_object_or_404(
            Lesson,
            slug = slug
        )

        context = {
            'lesson': lesson,
            'leaderboard': leaderboard,
            'subjects': subjects,
            'consecutive_days': consecutive_days
        }

        return render(request, 'training/lesson_detail.html', context)

    else:
        leaderboard = TestResult.objects.order_by('-score')[:10]

        languages = Language.objects.all()

        lesson = get_object_or_404(
            Lesson,
            slug = slug
        )

        context = {
            'lesson': lesson,
            'leaderboard': leaderboard,
            'languages': languages
        }

        return render(request, 'training/lesson_detail.html', context)



def subjects_view(request):
    if request.user.is_authenticated:
        try:
            user_klass = Profile.objects.get(user=request.user)
            subjects = Language.objects.filter(klass=user_klass.klass)
            return render(request, 'training/home.html', {'subjects': subjects})
        
        except Profile.DoesNotExist:
            return HttpResponse("Sizde Profil joq!")
    else:
        return redirect('sign_in')


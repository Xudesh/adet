from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .forms import *
from django.http import HttpResponse
from users.models import *
from training.models import *
from .models import *
from django.utils import timezone





@login_required
def quize_all(request):

    quize_different_lang = Language.objects.all()

    lesson_quizes = Lesson.objects.all()

    user = request.user
    today = timezone.now().date()

    if not DailyVisit.objects.filter(user=user, date_visited=today).exists():
                 
        DailyVisit.objects.create(user=user, date_visited=today)
    else:
        consecutive_days = DailyVisit.objects.filter(user=user, date_visited__lte=today).count()

    user_klass = Profile.objects.get(user=request.user) 
    subjects = Language.objects.filter(klass=user_klass.klass)

    leaderboard = TestResult.objects.order_by('-score')[:10]

    context = {
        'quizes_all': quize_different_lang,  
        'subjects': subjects,
        'leaderboard': leaderboard,
        'consecutive_days': consecutive_days,
        'lesson_quizes': lesson_quizes
    }

    return render(request, 'quizes/all.html', context)


@login_required
def test_view(request, subject_slug):

    user = request.user
    today = timezone.now().date()

    if not DailyVisit.objects.filter(user=user, date_visited=today).exists():
                 
        DailyVisit.objects.create(user=user, date_visited=today)
    else:
        consecutive_days = DailyVisit.objects.filter(user=user, date_visited__lte=today).count()

    questions = Question.objects.filter(language__subject_slug=subject_slug)

    

    form = TestForm(request.POST or None, questions=questions)

    user_klass = Profile.objects.get(user=request.user) 
    subjects = Language.objects.filter(klass=user_klass.klass)

    leaderboard = TestResult.objects.order_by('-score')[:10]


    if request.method == 'POST':
        if form.is_valid():
            # Создание или получение результатов теста для текущего пользователя
            test_result, created = TestResult.objects.get_or_create(user=request.user)
            
            # Обновление результатов теста и деталей теста
            test_result.score = form.calculate_score()
            test_result.save()

            for field_name, selected_answer_id in form.cleaned_data.items():
                question = Question.objects.get(id=int(field_name))
                selected_answer = Answer.objects.get(id=int(selected_answer_id))
                TestResultDetail.objects.create(test_result=test_result, question=question, selected_answer=selected_answer)

            return redirect('results', test_result.id)

    context = {
        'form': form, 
        'questions': questions,
        'subjects': subjects,
        'leaderboard': leaderboard,
        'consecutive_days': consecutive_days
    }

    return render(request, 'quizes/test.html', context)


@login_required
def pass_test(request, slug):
    questions = Question.objects.filter(lesson=slug)
    
    user = request.user
    today = timezone.now().date()

    if not DailyVisit.objects.filter(user=user, date_visited=today).exists():
                 
        DailyVisit.objects.create(user=user, date_visited=today)
    else:
        consecutive_days = DailyVisit.objects.filter(user=user, date_visited__lte=today).count()


    

    form = TestForm(request.POST or None, questions=questions)

    user_klass = Profile.objects.get(user=request.user) 
    subjects = Language.objects.filter(klass=user_klass.klass)

    leaderboard = TestResult.objects.order_by('-score')[:10]

    form = TestForm(request.POST, questions=questions)

    if request.method == "POST":

        if form.is_valid():
            # Создание или получение результатов теста для текущего пользователя
            test_result, created = TestResult.objects.get_or_create(user=request.user)
            
            # Обновление результатов теста и деталей теста
            test_result.score = form.calculate_score()
            test_result.save()

            for field_name, selected_answer_id in form.cleaned_data.items():
                question = Question.objects.get(id=int(field_name))
                selected_answer = Answer.objects.get(id=int(selected_answer_id))
                TestResultDetail.objects.create(test_result=test_result, question=question, selected_answer=selected_answer)

            return redirect('results', test_result.id)

        

    return render(request, "quizes/l_tests.html", 
    {
        "questions": questions,
        "form": form,
        'consecutive_days': consecutive_days,
        'leaderboard': leaderboard,
        'subjects': subjects
    })


def test_result(request, test_result_id):
    test_result = TestResult.objects.get(id=test_result_id)

    user = request.user
    today = timezone.now().date()

    if not DailyVisit.objects.filter(user=user, date_visited=today).exists():
                 
        DailyVisit.objects.create(user=user, date_visited=today)
    else:
        consecutive_days = DailyVisit.objects.filter(user=user, date_visited__lte=today).count()

    user_klass = Profile.objects.get(user=request.user) 

    subjects = Language.objects.filter(klass=user_klass.klass)

    leaderboard = TestResult.objects.order_by('-score')[:10]

    context = {
        'test_result': test_result,
        'consecutive_days': consecutive_days,
        'subjects': subjects,
        'leaderboard': leaderboard
        }

    return render(request, 'quizes/results.html', context)
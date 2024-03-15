from django.shortcuts import render
from .models import *



def AtaAnalar(request):
    parents = Parents.objects.all()

    context = {
        'parents': parents,
    }
    return render(request, 'bizler/ata_analar.html', context)


def teachers(request):
    return render(request, 'bizler/teachers.html')
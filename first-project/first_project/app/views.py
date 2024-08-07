import datetime
import os

from django.http import HttpResponse
from django.shortcuts import render, reverse


def home_view(request):
    template_name = 'app/home.html'
    # впишите правильные адреса страниц, используя
    # функцию `reverse`
    pages = {
        'Главная страница': reverse('home'),
        'Показать текущее время': 'current_time',
        'Показать содержимое рабочей директории': 'workdir'
    }
    
    # context и параметры render менять не нужно
    # подбробнее о них мы поговорим на следующих лекциях
    context = {
        'pages': pages
    }
    return render(request, template_name, context)


def time_view(request):
    now = datetime.datetime.now()
    time_1 = str(now).split(' ')
    time_1 = '-'.join(time_1)
    current_time = time_1[11:-7:]
    msg = f'Текущее время: {current_time}'
    return HttpResponse(msg)


def workdir_view(request):
    current_directory = os.getcwd()
    files_and_dirs = os.listdir(current_directory)
    files_string = ", ".join(files_and_dirs)
    msg = f'Содержимое рабочей директории: {files_string}'
    return HttpResponse(msg)

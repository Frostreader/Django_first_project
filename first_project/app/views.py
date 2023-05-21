import os

from django.http import HttpResponse
from django.shortcuts import render, reverse
from datetime import datetime
import pytz


def home_view(request):
    template_name = 'app/home.html'
    # впишите правильные адреса страниц, используя
    # функцию `reverse`
    pages = {
        'Главная страница': reverse('home'),
        'Показать текущее время': reverse('time'),
        'Показать содержимое рабочей директории': reverse('workdir')
    }

    # context и параметры render менять не нужно
    # подбробнее о них мы поговорим на следующих лекциях
    context = {
        'pages': pages
    }
    return render(request, template_name, context)


def time_view(request):
    # обратите внимание – здесь HTML шаблона нет,
    # возвращается просто текст
    tz = pytz.timezone('Europe/Moscow')
    current_time = datetime.now(tz).strftime('%H:%M')
    msg = f'Текущее время: {current_time}'
    return HttpResponse(str(msg))


def workdir_view(request):
    # по аналогии с `time_view`, напишите код,
    # который возвращает список файлов в рабочей
    # директории
    files = os.listdir()
    file_list = {
        'files': files
    }
    return render(request, 'app/workdir.html', file_list)

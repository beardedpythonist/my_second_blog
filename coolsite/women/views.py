from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import render, redirect

from .models import *

menu = [{'title': 'О сайте', 'url_name': 'about'},
        {'title': 'добавить статью', 'url_name': 'add_page'},
        {'title': 'обратная связь', 'url_name': 'contact'},
        {'title': 'войти', 'url_name': 'login'}]


def index11(request):
    post = Women.objects.all()
    cats = Category.objects.all()
    context = {'post': post,
               'menu': menu,
               'title5': 'Главная страница))))))',
               'cat_selected':0}




    return render(request, 'women/index.html', context=context)


def about(request):
    return render(request, 'women/about.html', {'menu': menu, 'title5': 'О сайте....'})


def addpage(request):
    return HttpResponse('дОбавление статьи')

def contact(request):
    return HttpResponse('Обратная связь')

def login(request):
    return HttpResponse('Авторизация')



def show_post(request, post_id):
    return HttpResponse(f' Отображение статьи с id= {post_id}')


def show_category(request, cat_id):
    return HttpResponse(f' Отображение статьи с id= {cat_id}')




def pagenotfound(request, exception):
    return HttpResponseNotFound('страница не найдена')

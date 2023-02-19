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
               'cats': cats,
               'title5': 'Главная страница))))))',
               'cat_selected':0}
    return render(request, 'women/index.html', context=context)


def about(request):
    return render(request, 'women/about.html', {'menu': menu})


def addpage(request):
    return HttpResponse('дОбавление статьи')

def contact(request):
    return HttpResponse('Обратная связь')

def login(request):
    return HttpResponse('Авторизация')

def show_post(request, cat_id):
    pass


def show_category(request, cat_id):
    post = Women.objects.filter(cat_id=cat_id)
    cats = Category.objects.all()
    if len(post) == 0:
        raise Http404()

    context = {'post': post,
               'menu': menu,
               'cats': cats,
               'title5': 'отображение по рубрикам',
               'cat_selected': cat_id}
    return render(request, 'women/index.html', context=context)


def pageNotFound(request, exception):
    return HttpResponseNotFound(' <h1> страница не найдена  </h1>')
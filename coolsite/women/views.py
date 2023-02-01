from django.shortcuts import render,  redirect
from django.http import HttpResponse,  HttpResponseNotFound, Http404
from .models import *


menu = ['О сайте','добавить статью','обратная связь','войти']
def index11(request):
    post = Women.objects.all()
    return render(request, 'women/index.html', {'post': post, 'menu': menu, 'title5':'Главная страница))))))'})


def about(request):
    return render(request, 'women/about.html', {'menu': menu, 'title5':'О сайте....'})

def categories(request, catid):
    return HttpResponse(f'<h1>статьи по категориям</h1>   <p> {catid}</p>')

def archive(request, year):
    if int(year) > 2020:
        return redirect('home', permanent=True)
    return HttpResponse(f'<h1> Архив по годам </h1>  <p> {year}</p>')


def pagenotfound(request, exception):
    return HttpResponseNotFound('страница не найдена')
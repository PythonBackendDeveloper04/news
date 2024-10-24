from django.shortcuts import render,get_object_or_404
from django.views.generic import ListView
from .models import News,Category

def news_list(request):
    #news_list = News.published.all()
    news_list = News.objects.filter(status=News.Status.Published)
    context = {
        'news_list':news_list
    }
    return render(request,'index.html',context=context)
def news_detail(request,id):
    news = get_object_or_404(News,id=id,status=News.Status.Published)
    context = {
        'news':news
    }
    return render(request,'single_page.html',context=context)

def indexView(request):
    news = News.objects.filter(status=News.Status.Published)
    categories = Category.objects.all()
    context = {
        'news':news,
        'categories':categories
    }
    return render(request,'index.html',context=context)

def contact(request):
    context = {

    }
    return render(request,'contact.html',context=context)
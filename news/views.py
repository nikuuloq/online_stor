from django.shortcuts import render

from news.models import News

def new_list(request):
    news = News.objects.order_by("-created_at")
    return render(request, "news_list.html", context={"news": news })

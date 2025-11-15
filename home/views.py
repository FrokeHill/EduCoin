from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import User, Item, News
from django.db.models import Count
from .utils import get_student


def index(request):
    if request.user.is_authenticated:
        user = request.user
        
        if user.is_teacher:
            context = {
                "started_at": user.started_at,
                "user_type": "teacher",
                "username": user.username,
                "full_name": user.get_full_name() or user.username
            }
            return render(request, "index.html", context=context)
            
        elif user.is_student:
            item = Item.objects.all()
            coin_obj = user.coins.first()
            total_coins = coin_obj.count if coin_obj else 0
            groups = user.student_groups.all()
            news = News.objects.all()
            
            
            studentlar = User.objects.filter(
                user_type='student',
                
                coins__isnull=False
            ).annotate(
                coin_count=Count("coins")
            ).order_by("-coin_count")
            
            user_rank = 0 
            for index, student in enumerate(studentlar, start=1):
                if student.id == user.id:
                    user_rank = index
                    break
            
            context = {
                "coin": total_coins,
                "user_type": "student",
                "username": user.username,
                "full_name": user.get_full_name() or user.username,
                "t_yil": user.t_yil,
                "groups": groups,
                "rank": user_rank,
                "items": item, 
                "news": news,
            }
            return render(request, "index.html", context=context)
        else:
            return render(request, "index.html")
    else:
        return redirect('student_login')
def allNews(request):
    news = News.objects.all()
    context = {
        "news": news
    }
    return render(request, "all_news.html", context=context)
def detail(request, product_id):
    new = News.objects.get(id=product_id)
    context = {
        "new": new
    }
    return render(request, "news_detail.html", context=context)
def market(request):
    products = Item.objects.filter(total__isnull=False)
   
    abs1 = {
        "items": products,
        "isactive":"active",
    }
    abs2 = get_student(request)
   
    context = abs1 | abs2


    return render(request, "market.html", context )

    
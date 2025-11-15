from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UserForm
from home.models import User, Item, Purchase
from django.db.models import Count
from home.utils import get_student

def student_login(request):
    if request.method == "GET":
        return render(request, "student_login.html")

    elif request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        try:
            user = authenticate(request=request, username=username, password=password)

            if user is not None and user.is_student:
                login(request, user)
                messages.success(request, "login qildingiz")
                print("student logged in")
                return redirect("homepage")

            elif user is not None and user.is_teacher:
                messages.error(request, "Siz student emassiz! Teacher login dan foydalaning.")
                print("user is a teacher")
                return render(request, "teacher_login.html")

            else:
                messages.error(request, "Use'rname yoki parol noto'gri!")
                print("parol noto'g'ri")
                return render(request, "student_login.html")

        except Exception as e:
            messages.error(request, "Xatolik yuz berdi!")
            print(f"Error: {e}")
            return render(request, "student_login.html")


# @login_required()
# def student_profile(request):

#     user = request.user
#     coin_obj = user.coins.first()
#     total_coins = coin_obj.count if coin_obj else 0
#     groups = user.student_groups.all()
#     transactions = user.transactions_set.all().order_by('-created_at')
    
#     studentlar = User.objects.filter(
#     user_type='student',
    
#     coins__isnull=False
#     ).annotate(
#         coin_count=Count("coins")
#     ).order_by("-coin_count")

#     user_rank = 0 
#     for index, student in enumerate(studentlar, start=1):
#         if student.id == user.id:
#             user_rank = index
#             break
    
#     context = {
#         "total_coins": total_coins,
#         "groups": groups,
#         "transactions": transactions,
#         "user_type": "student",
#         "username": user.username,
#         "full_name": user.get_full_name() or user.username,
#         "t_yil": user.t_yil,
#         "phone": user.phone,
#         "email": user.email,
#         "rank": user_rank
#     }
#     return render(request, "student_profile_page.html", context=context)
@login_required()
def student_profile(request):

    student = get_student(request)
    
    
    return render(request, "student_profile_page.html", context=student)


@login_required
def student_logout(request):
    logout(request)


    messages.success(request, "Tizimdan chiqdingiz")


    return redirect("student_login")

def student_update(request):
    user = request.user

    if request.method == "POST":
        form = UserForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            return redirect('../student_profile')
    else:
        form = UserForm(instance=user)

    return render(request, "student_update.html", {"form": form})

@login_required # type: ignore
def item_buy(request, id):
    user = get_student(request)
    coin = user["coin"]
    item = Item.objects.filter(id=id, total__isnull=False, price__lte=coin).first()

    if item:
        Purchase.objects.create(
            student=request.user,
            maxsulot=item,
        )
        coin -= item.price
        messages.info(request, "Sotib olindi")

        return redirect("student_profile")
    
    else:
        messages.info(request, "Sotib olib bo'lmaydi")

        return redirect("student_profile")

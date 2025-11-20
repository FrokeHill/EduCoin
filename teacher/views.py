from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages
from home.utils import get_teacher
from home.models import Group

def teacher_login(request):
    if request.method == "GET":
        return render(request, "teacher_login.html")

    elif request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        try:
            user = authenticate(request=request, username=username, password=password)

            if user is not None and user.is_teacher:
                login(request, user)
                messages.success(request, "Muvaffaqiyatli login qildingiz!")
                print("teacher logged in")
                return redirect("homepage")
            elif user is not None and user.is_student:
                messages.error(request, "Siz teacher emassiz! Student login dan foydalaning.")
                print("user is a student")
                return render(request, "student_login.html")
            else:
                messages.error(request, "Username yoki parol noto'g'ri!")
                print("parol noto'g'ri")
                return render(request, "teacher_login.html")
        except Exception as e:
            messages.error(request, "Xatolik yuz berdi!")
            print(f"Error: {e}")
            return render(request, "teacher_login.html")


def coin_berish(request):
    context = get_teacher(request)
    
    return render(request, "coin_berish.html", context=context)


def group(request, id):
    context = get_teacher(request)
    group_detail = Group.objects.get(id=id)

    context["group_detail"] = group_detail

    return render(request, "group_detail.html", context=context)

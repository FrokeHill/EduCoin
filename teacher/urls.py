from django.urls import path
from .views import teacher_login

urlpatterns = [
    path('teacher_login/', teacher_login, name="teacher_login"),






    # path('logout/', teacher_logout, name="teacher_logout"),
]

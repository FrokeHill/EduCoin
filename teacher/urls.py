from django.urls import path
from .views import teacher_login, coin_berish, group

urlpatterns = [
    path('teacher_login/', teacher_login, name="teacher_login"),
    path('coin_berish/', coin_berish, name="coin_berish"),
    path("group/<uuid:id>", group, name="group")





    # path('logout/', teacher_logout, name="teacher_logout"),
]

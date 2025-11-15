from django.urls import path
from .views import student_login, student_profile, student_logout, student_update, item_buy

urlpatterns = [
    path("student_login", student_login, name="student_login"),
    path("student_profile", student_profile, name="student_profile"),
    path("student_logout", student_logout, name="student_logout"),
    path('student_update/', student_update, name='student_update'),  
    path("item_buy/<uuid:id>", item_buy, name="item_buy"),
]

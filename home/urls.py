from django.urls import path
from .views import index, allNews,detail,market

urlpatterns = [
    path('', index, name="homepage"),
    path('allnews', allNews, name="allnews"),
    path('detail/<int:product_id>/',detail ),
    path('market/', market, name="marketpage"),
]



from django.urls import path
from .views import news_list,news_detail,indexView,contact

urlpatterns = [
    path("",indexView,name='index'),
    path("<int:pk>/",news_detail,name='news_detail'),
    path("contacts/",contact,name='contact_pg')
]
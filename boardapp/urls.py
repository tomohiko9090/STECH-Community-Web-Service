from django.urls import path, include
from .views import signupfunc, loginfunc, listfunc, logoutfunc, detailfunc, goodfunc, readfunc, BoardCreate, like_listfunc, chat_listfunc, IndexView, ItemDetailView, addItem, OrderView

urlpatterns = [
    path('signup/', signupfunc, name='signup'),
    path('login/', loginfunc, name='login'),
    path('list/', listfunc, name='list'),
    path('login/', logoutfunc, name='logout'),
    path('detail/<int:pk>', detailfunc, name='detail'),
    path('good/<int:pk>', goodfunc, name='good'),
    path('read/<int:pk>', readfunc, name='read'),
    path('create/', BoardCreate.as_view(), name='create'),
    path('like_list/', like_listfunc, name="like_list"),
    path('chat_list/', chat_listfunc, name='chat_list'),
    path('index/', IndexView.as_view(),name = 'index'),
    path('product/<slug>', ItemDetailView.as_view(),name = 'product'),
    path('additem/<slug>', addItem ,name = 'additem'), 
    path('order/', OrderView.as_view(),name = 'order'), 
]
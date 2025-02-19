from django.urls import path
from . import views

urlpatterns=[

    path('',views.index, name='home'),
    path('create_book',views.BookCreate.as_view(),name='create_book'),
     path('create_author',views.AuthorCreate.as_view(),name='create_author'),
    path('book/<int:pk>',views.BookDetail,name='book_detail'),
    path('my_view',views.my_view,name='my_view'),
    path('signup', views.SignUpView.as_view(),name='signup'),
    path('profile/',views.CheckedOutBooksByUser.as_view(),name='profile'),
    path('list_books',views.AllBooks.as_view(),name='list_books')
]
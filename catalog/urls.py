from django.urls import path
from . import views

urlpatterns=[

    path('',views.index, name='home'),
    path('create_book',views.BookCreate.as_view(),name='correct_book'),
    path('book/<int:pk>',views.BookDetail.as_view(),name='book_detail'),
    path('my_view',views.my_view,name='my_view'),
    path('signup', views.SignUpView.as_view(),name='signup'),
    path('profile/',views.CheckedOutBooksByUser.as_view(),name='profile')
]
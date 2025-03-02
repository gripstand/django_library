from django.urls import path
from . import views

urlpatterns=[

    path('',views.index, name='home'),
    path('create_book',views.BookCreate.as_view(),name='create_book'),
    path('create_author',views.AuthorCreate.as_view(),name='create_author'),
    path('create_genre',views.GenreCreate.as_view(),name='create_genre'),
    path('book/<int:pk>',views.BookDetail,name='book_detail'),
    path('my_view',views.my_view,name='my_view'),
    path('signup', views.SignUpView.as_view(),name='signup'),
    path('profile/',views.CheckedOutBooksByUser.as_view(),name='profile'),
    path('list_authors',views.AllAuthors.as_view(),name='list_authors'),
    path('update_author/<int:pk>', views.AuthorUpdate.as_view(),name='update_author'),
    path('delete_author/<int:pk>', views.AuthorDelete.as_view(),name='delete_author'),
    path('update_book/<int:pk>', views.BookUpdate.as_view(),name='update_book'),
    path('delete_book/<int:pk>', views.BookDelete.as_view(),name='delete_book'),
    path('create_instance', views.InstanceCreate.as_view(),name='create_instance'),
    path('list_books', views.ListBookDetails,name='list_books'),
    path('list_instance_details/<int:pk>', views.ListInstances.as_view(),name='list_instance_details'),
    path('create_book_instance/<int:book_id>', views.InstanceCreate.as_view(),name='create_book_instance'),
]
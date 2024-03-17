from django.urls import path

from bookstore.views import home , list_books , profile , books_index , show,add , delete,edit

urlpatterns = [

    path('home', home, name='bookstore.home' ),
    path('books', list_books, name='bookstore.books' ),
    path('<int:id>', profile, name='bookstore.profile'),
    path('books2', books_index ,  name='bookstore.books2' ),
    path('books2/<int:id>', show, name='bookstore.show' ),
    path('add', add, name='bookstore.add'),
    path('books2/<int:id>/delete', delete, name='bookstore.delete'),

    path('books2/<int:id>/edit', edit, name='bookstore.edit'),
    




]
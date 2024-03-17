from django.urls import path
from author.views import home , add , show , delete , edit

urlpatterns = [

    path('home', home, name='author.home' ),
    # path('books', list_books, name='bookstore.books' ),
    # path('<int:id>', profile, name='bookstore.profile'),
    # path('books2', books_index ,  name='bookstore.books2' ),
    path('home/<int:id>', show, name='author.show' ),
    path('add', add, name='author.add'),
    path('home/<int:id>/delete', delete, name='author.delete'),

    path('home/<int:id>/edit', edit, name='author.edit'),
    




]
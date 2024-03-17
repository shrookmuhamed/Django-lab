from django.shortcuts import render , redirect, reverse
from django.http import HttpResponse
from bookstore.models import book
from .forms import BookForm
from django.contrib.auth.decorators import login_required

def profile(request , id ):
    filtered_books = filter(lambda book: book["id"] == id, books)
    filtered_books = list(filtered_books)
    print(filtered_books)
    if filtered_books:
        return render(request,
                      'bookstore/profile.html',
                      context= {"book":filtered_books[0]})
    return HttpResponse("Book not found")


def home(request):
    return render(request,"bookstore/home.html")
books = [
    {"id":1 , "name": "Harry Potter and the Philosopher's Stone", "price":"200","image":"philo.jpg","author":"J.K. Rowling","pages":"223"},
    {"id":2 , "name": "Harry Potter and the Chamber of Secrets", "price":"200","image":"champer.jpg","author":"J.K. Rowling","pages":"251"},
    {"id":3 , "name": "Harry Potter and the Prisoner of Azkaban", "price":"200","image":"azk.jpg","author":"J.K. Rowling","pages":"317"},
    {"id":4 , "name": "Harry Potter and the the Goblet of Fire", "price":"200","image":"g.png","author":"J.K. Rowling","pages":"636"}
]               
def list_books(request):
    return render(request,"bookstore/books.html", context= {"books":books })  

def books_index(request):
    books = book.objects.all()
    return render(request,
                  'bookstore/day2book.html',
              context={"books":books})  

def show(request, id):
    books = book.objects.get(id=id)
    return render(request, 'bookstore/show.html',
                  context={"book":books})    

# def add(request):
#     form = BookForm()

#     if request.method == 'POST':
#         form = BookForm(request.POST, request.FILES)
#         if form.is_valid():
#             form.save() 
            
#             url = reverse("bookstore.books2")
#             return redirect(url)
#         return render(request, 'bookstore/add.html',context={"form":form})
#     return render(request, 'bookstore/add.html')
# from .forms import BookForm
@login_required(login_url='/users/login')
def add(request):
    form = BookForm()

    if request.method == 'POST':
        form = BookForm(request.POST, request.FILES)
        if form.is_valid():
            form.save() 
            url = reverse("bookstore.books2")
            return redirect(url)
            # Redirect to a success URL
    return render(request, 'bookstore/add.html', {'form': form})


    # if request.method == 'POST':
    #     ## get info about image uploaded  request.FILES
    #     print(request.FILES)
    #     print(request.POST) # to get data entered in the form
    #     name = request.POST["name"]
    #     price = request.POST["price"]
    #     pages = request.POST["pages"]
    #     # image = request.POST["image"]
    #     books = book()
    #     books.name = name
    #     books.price = price
    #     books.pages = pages
    #     books.image = request.FILES['image']
    #     books.save()
    #     url = reverse("bookstore.books2")
    #     return redirect(url)

    # # request GET
    # return render(request, 'bookstore/add.html')
@login_required(login_url='/users/login')
def delete(request, id):
    books = book.objects.get(id=id)
    books.delete()
    url = reverse("bookstore.books2")
    return redirect(url)
@login_required(login_url='/users/login')
def edit(request, id):
    books = book.objects.get(id=id)

    if request.method == 'POST':
        form = BookForm(request.POST, request.FILES, instance=books)
        
        if form.is_valid():
            form.save()
            url = reverse("bookstore.books2")
            return redirect(url)
    else:
        form = BookForm(instance=books)
    return render(request, 'bookstore/edit.html', {'form': form, 'book': books})

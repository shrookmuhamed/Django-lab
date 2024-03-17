
# Create your views here.
from django.shortcuts import render , reverse , redirect , get_object_or_404
from django.http import  HttpResponse
from django.contrib.auth.decorators import login_required

from author.models import author
from author.forms import AuthorForm

# # Create your views here.


def home(request):
    authors = author.objects.all() 
    return render(request, "author/authors.html", {"authors": authors})


def show(request,id):
    authors = author.objects.get(id=id)
      # Access related books
    return render(request, "author/show.html", context={"authors":authors})
@login_required(login_url='/users/login')
def add(request):
    if request.method == 'POST':
        ## get info about image uploaded  request.FILES
        print(request.FILES)
        print(request.POST) # to get data entered in the form
        name = request.POST["name"]
        # image = request.POST["image"]
        authors = author()
        authors.name = name
        authors.image = request.FILES['image']
        authors.save()
        url = reverse("author.home")
        return redirect(url)

    # request GET
    return render(request, 'author/add.html')

@login_required(login_url='/users/login')
def delete(request, id):
    authors = author.objects.get(id=id)
    authors.delete()
    url = reverse("author.home")
    return redirect(url)
@login_required(login_url='/users/login')
def edit(request, id):
    authors = author.objects.get(id=id)

    if request.method == 'POST':
        form = AuthorForm(request.POST, request.FILES, instance=authors)
        
        if form.is_valid():
            form.save()
            url = reverse("author.home")
            return redirect(url)
    else:
        form = AuthorForm(instance=authors)
    return render(request, 'author/edit.html', {'form': form, 'author': authors})

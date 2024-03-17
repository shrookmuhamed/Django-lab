from django.shortcuts import render, redirect, reverse
from django.http import HttpResponse
from users.forms import  UserModelForm
# Create your views here.
from django.contrib.auth.views import LogoutView
from django.urls import reverse_lazy
from django.http import HttpResponseRedirect

class CustomLogoutView(LogoutView):
    next_page = reverse_lazy('bookstore.home')  # Change 'home' to the name of your home page URL pattern

    def get_next_page(self):
        next_page = self.next_page
        if self.redirect_field_name in self.request.POST:
            next_page = self.request.POST[self.redirect_field_name]
        return next_page



def profile(request):
    url = reverse('bookstore.books2')
    return redirect(url)
    # return HttpResponse("Login successfully ")

# def logout(request):
#     url = reverse('bookstore.home')
#     return redirect(url)
#     # return HttpResponse("Login successfully ")


   


def create_user(request):
    form = UserModelForm()
    if request.method=='POST':
        form = UserModelForm(request.POST)
        if form.is_valid():
            form.save()
        url = reverse('bookstore.home')
        return redirect(url)
    return render(request,
                  'users/create_user.html', {'form': form})

from django.contrib.auth import authenticate,login,logout
from django.shortcuts import render, redirect
from item.models import Category,Item
from .forms import SignupForm

# Create your views here.

def index(request):
    items = Item.objects.filter(is_sold=False)[0:6]
    categories = Category.objects.all()
    return render(request, 'core/index.html',{
        'categories':categories,
        'items':items
    })

def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)

        if form.is_valid():
            form.save()

            return redirect('/login/')
    else:
        form = SignupForm()

    return render(request, 'core/signup.html', {
        'form': form
    })

def logout_view(request):
    logout(request)
    return redirect("/login/")

def custom_404_view(request, exception=None):
    return render(request, 'core/404.html',status=404)
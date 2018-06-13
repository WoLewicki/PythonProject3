from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect

from .models import Question, Response, Category, User


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('/logout')
    else:
        form = UserCreationForm()
    return render(request, 'login/register.html', {'form': form})


def home(request):
    categories = Category.objects.order_by('name')
    return render(request, 'home/main_page.html', {'categories_list': categories})


def category_page(request):
    questions = Question.objects.order_by('pub_date')
    return render(request, 'home/category_page.html', {'questions_list': questions})
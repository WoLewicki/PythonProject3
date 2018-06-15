from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.utils import timezone
from django.contrib.auth.decorators import login_required

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
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'login/register.html', {'form': form})


@login_required
def home(request):
    categories = Category.objects.order_by('name')
    return render(request, 'home/main_page.html', {'categories_list': categories})


@login_required
def category_page(request, category_name):
    questions = Question.objects.order_by('pub_date').filter(category__name=category_name)
    return render(request, 'home/category_page.html', {'questions_list': questions})


@login_required
def new_question(request):
    categories = Category.objects.order_by('name')
    return render(request, 'home/new_question.html', {'categories_list': categories})


@login_required
def add_question(request):
    topic = request.POST.get('topic')
    text = request.POST.get('text')
    category = request.POST.get('category')
    category = Category.objects.get(id=int(category))
    question = Question(topic=topic, user=request.user, category=category, question_text=text, pub_date=timezone.now())
    question.save()
    return redirect('/home/'+category.name)


@login_required
def show_question(request, question_category, question_id):
    responses = Response.objects.order_by('-like_counter').filter(question__id=question_id)
    question_topic = Question.objects.get(id=question_id).topic
    question_text = Question.objects.get(id=question_id).question_text
    pub_date = Question.objects.get(id=question_id).pub_date
    return render(request, 'home/question_page.html', {'responses_list': responses, 'question_topic': question_topic, 
                                                       'question_text': question_text, 'question_id': question_id,
                                                       'category_name': question_category, 'pub_date': pub_date})


@login_required
def new_response(request, question_id):
    return render(request, 'home/new_response.html', {'question_id': question_id})


@login_required
def add_response(request, question_id):
    text = request.POST.get('text')
    question = Question.objects.get(id=int(question_id))
    category_name = Question.objects.get(id=int(question_id)).category
    category_name = category_name.name
    response = Response(user=request.user, question=question, message_text=text, like_counter=0, pub_date=timezone.now())
    response.save()
    return redirect('/home/'+category_name+'/'+question_id+'/')


@login_required
def vote(request, category_name, question_id, response_id, plus_or_minus):
    response = Response.objects.get(id=response_id)
    if plus_or_minus == '+':
        response.like_counter += 1
    elif plus_or_minus == '-':
        response.like_counter -= 1
    response.save()
    return redirect('/home/' + category_name + '/' + question_id + '/')


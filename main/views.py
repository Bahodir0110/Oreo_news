from django.shortcuts import render, redirect
from .models import Articles
from .forms import ArticlesForm
from django.views.generic import DetailView
from . import forms

def index(request):
    news = Articles.objects.order_by('-date')
    return render(request, 'main/index.html', {"news": news})


class NewsDetailView(DetailView):
    model = Articles
    template_name = 'main/details_view.html'
    context_object_name = 'article'


def about(request):
    return render(request, 'main/about.html')


def contacts(request):
    return render(request, 'main/contacts.html')


def create(request):
    error = ''
    if request.method == 'POST':
        form = ArticlesForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            error = 'Incorrect Form'

    form = ArticlesForm

    data = {
        'form': form,
        'error': error
    }
    return render(request, 'main/create.html', data)


def register(request):
    if request.method == 'POST':
        form = forms.RegisterForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/')
    else:
        form =forms.RegisterForm()
        return render(request, 'registration/register.html', {'form': form})
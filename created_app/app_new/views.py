from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Author
from .models import Quote


# Create your views here.
def index(request):
    return render(request, "app_new/index.html", context={"author.name": "Main Page"})

def add_author(request):
    # код для додавання нового автора
    pass

@login_required
def add_quote(request):
    # код для додавання нової цитати
    pass

def author_detail(request, author_id):
    author = Author.objects.get(pk=author_id)
    return render(request, 'author_detail.html', {'author': author})

def all_quotes(request):
    quotes = Quote.objects.all()
    return render(request, 'all_quotes.html', {'quotes': quotes})
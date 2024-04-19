from django.http import HttpResponse
from django.shortcuts import render
import json


booksData = open(
    r'E:\Tutorial\django\bitfumes\django-course\bookstore_app\books.json').read()


data = json.loads(booksData)
# Create your views here.


def index(request):
    context = {'books': data}
    return render(request, 'bookstore/index.html', context)

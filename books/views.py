from datetime import datetime

from django.shortcuts import render, redirect
from django.urls import register_converter

from books.models import Book


class DateConverter:
    regex = r'[0-9]{4}-[0-9]{2}-[0-9]{2}'
    format = '%Y-%m-%d'

    def to_python(self, value: str) -> datetime:
        return datetime.strptime(value, self.format)

    def to_url(self, value: datetime) -> str:
        return value.strftime(self.format)


register_converter(DateConverter, 'date')

sorted_list_dates = []
dates = list(Book.objects.dates('pub_date', 'day'))
for line in dates:
    data = line.isoformat()
    sorted_list_dates.append(data)
length = len(sorted_list_dates) - 1


def index(request):
    return redirect('books')


def books_view(request):
    template = 'books/books_list.html'
    books = Book.objects.all()
    context = {
        'books': books
    }
    return render(request, template, context)


def show_books(request, dt):
    template = 'books/public_dates.html'
    dt_str = dt.strftime('%Y-%m-%d')
    index = sorted_list_dates.index(dt_str)
    if index == 0:
        page = {'previous_page': False, 'next_page': sorted_list_dates[index + 1]}
    elif index == length:
        page = {'previous_page': sorted_list_dates[index - 1], 'next_page': False}
    else:
        page = {'previous_page': sorted_list_dates[index - 1], 'next_page': sorted_list_dates[index + 1]}

    book = Book.objects.filter(pub_date=dt)
    context = {
        'books': book,
        'page': page
    }
    return render(request, template, context)

from django.core.management import BaseCommand

from books.models import Book


class Command(BaseCommand):
    help = 'Заполнение базы данных'

    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):
        books = [{'name': 'Скотный двор', 'author': 'Джордж Оруэл', 'pub_date': '2018-09-21'},
                 {'name': 'В память о прошлом земли', 'author': 'Лю Цысинь', 'pub_date': '2018-09-21'}]
        for book in books:
            Book.objects.create(
                name=book['name'],
                author=book['author'],
                pub_date=book['pub_date']
            )
            self.stdout.write(f'Автор {book["author"]} загружен')

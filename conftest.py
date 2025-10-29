import pytest
from main import BooksCollector


class TestBooksCollector:

    @pytest.fixture
    def adding_books_and_genres(self):
        collector = BooksCollector()
        collector.add_new_book("Оно")
        collector.add_new_book("Шерлок")
        collector.add_new_book("Звездные войны")
        collector.set_book_genre("Оно", "Ужасы")
        collector.set_book_genre("Шерлок", "Детективы")
        collector.set_book_genre("Звездные войны", "Фантастика")

        return collector

    @pytest.fixture
    def adding_favourites(self):
        collector = BooksCollector()
        collector.add_new_book("Оно")
        collector.add_new_book("Звездные войны")
        collector.add_book_in_favorites("Оно")
        collector.add_book_in_favorites("Звездные войны")
        return collector

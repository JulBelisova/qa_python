import pytest
from main import BooksCollector


class TestBooksCollector:

    @pytest.fixture
    def collector(self):
        collector = BooksCollector()

        return collector

    @pytest.mark.parametrize("name", ["Шерлок", "Оно", "Звездные войны"])
    def test_add_new_book_with_valid_names(self, name, collector):
        collector.add_new_book(name)
        assert name in collector.books_genre

    def test_set_book_genre_add_for_existing_book(self, collector):
        collector.add_new_book("Оно")
        collector.set_book_genre("Оно", "Ужасы")

        assert collector.books_genre["Оно"] == "Ужасы"

    def test_get_book_genre_for_existing_book(self, collector):
        collector.add_new_book("Оно")
        collector.add_new_book("Шерлок")
        collector.add_new_book("Звездные войны")
        collector.set_book_genre("Оно", "Ужасы")
        collector.set_book_genre("Шерлок", "Детективы")
        collector.set_book_genre("Звездные войны", "Фантастика")

        assert collector.get_book_genre("Оно") == "Ужасы"

    def test_get_books_with_specific_genre_horror(self, collector):
        collector.add_new_book("Оно")
        collector.add_new_book("Шерлок")
        collector.add_new_book("Звездные войны")
        collector.set_book_genre("Оно", "Ужасы")
        collector.set_book_genre("Шерлок", "Детективы")
        collector.set_book_genre("Звездные войны", "Фантастика")

        assert collector.get_books_with_specific_genre("Ужасы") == ["Оно"]

    def test_get_books_genre(self, collector):
        collector.add_new_book("Оно")
        collector.add_new_book("Шерлок")
        collector.add_new_book("Звездные войны")
        collector.set_book_genre("Оно", "Ужасы")
        collector.set_book_genre("Шерлок", "Детективы")
        collector.set_book_genre("Звездные войны", "Фантастика")
        result = {"Оно": "Ужасы", "Шерлок": "Детективы", "Звездные войны": "Фантастика"}

        assert collector.get_books_genre() == result

    def test_get_books_for_children_where_they_are_not_genre_age_rating(
        self, collector
    ):
        collector.add_new_book("Оно")
        collector.add_new_book("Шерлок")
        collector.add_new_book("Звездные войны")
        collector.set_book_genre("Оно", "Ужасы")
        collector.set_book_genre("Шерлок", "Детективы")
        collector.set_book_genre("Звездные войны", "Фантастика")

        assert collector.get_books_for_children() == ["Звездные войны"]

    def test_add_book_in_favorites_when_name_is_not_in_favorites(self, collector):
        collector.add_new_book("Оно")
        collector.add_new_book("Шерлок")
        collector.add_new_book("Звездные войны")
        collector.set_book_genre("Оно", "Ужасы")
        collector.set_book_genre("Шерлок", "Детективы")
        collector.set_book_genre("Звездные войны", "Фантастика")
        collector.add_book_in_favorites("Оно")

        assert collector.favorites == ["Оно"]

    def test_delete_book_from_favorites_multiple_books(self, collector):
        collector.add_new_book("Оно")
        collector.add_new_book("Звездные войны")
        collector.add_book_in_favorites("Оно")
        collector.add_book_in_favorites("Звездные войны")
        collector.delete_book_from_favorites("Звездные войны")

        assert collector.favorites == ["Оно"]

    def test_get_list_of_favorites_books_list_is_full(self, collector):
        collector.add_new_book("Оно")
        collector.add_new_book("Звездные войны")
        collector.add_book_in_favorites("Оно")
        collector.add_book_in_favorites("Звездные войны")
        assert collector.get_list_of_favorites_books() == [
            "Оно",
            "Звездные войны",
        ]

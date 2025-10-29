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

    @pytest.mark.parametrize("name", ["Шерлок", "Оно", "Звездные войны"])
    def test_add_new_book_with_valid_names(self, name):
        collector = BooksCollector()
        collector.add_new_book(name)
        assert name in collector.books_genre

    def test_set_book_genre_add_for_existing_book(self):
        collector = BooksCollector()
        collector.add_new_book("Оно")
        collector.set_book_genre("Оно", "Ужасы")

        assert collector.books_genre["Оно"] == "Ужасы"

    def test_get_book_genre_for_existing_book(self, adding_books_and_genres):
        assert adding_books_and_genres.get_book_genre("Оно") == "Ужасы"

    def test_get_books_with_specific_genre_horror(self, adding_books_and_genres):
        assert adding_books_and_genres.get_books_with_specific_genre("Ужасы") == ["Оно"]

    def test_get_books_genre(self, adding_books_and_genres):
        result = {"Оно": "Ужасы", "Шерлок": "Детективы", "Звездные войны": "Фантастика"}
        assert adding_books_and_genres.get_books_genre() == result

    def test_get_books_for_children_where_they_are_not_genre_age_rating(
        self, adding_books_and_genres
    ):
        assert adding_books_and_genres.get_books_for_children() == ["Звездные войны"]

    def test_add_book_in_favorites_when_name_is_not_in_favorites(
        self, adding_books_and_genres
    ):
        adding_books_and_genres.add_book_in_favorites("Оно")
        assert adding_books_and_genres.favorites == ["Оно"]

    def test_delete_book_from_favorites_multiple_books(self, adding_favourites):
        adding_favourites.delete_book_from_favorites("Звездные войны")

        assert adding_favourites.favorites == ["Оно"]

    def test_get_list_of_favorites_books_list_is_full(self, adding_favourites):

        assert adding_favourites.get_list_of_favorites_books() == [
            "Оно",
            "Звездные войны",
        ]

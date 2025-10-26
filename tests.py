from main import BooksCollector


class TestBooksCollector:

    import pytest

    @pytest.mark.parametrize(
        "name,genre",
        [("Шерлок", "Детективы"), ("Оно", "Ужасы"), ("Звездные войны", "Фантастика")],
    )
    def test_set_book_genre_add_existed_name_and_genre(self, name, genre):
        collector = BooksCollector()
        collector.add_new_book(name)
        collector.set_book_genre(name, genre)

        assert collector.books_genre[name] == genre

    def test_get_book_genre_for_existing_book(self):
        collector = BooksCollector()
        collector.add_new_book("Оно")
        collector.set_book_genre("Оно", "Ужасы")

        assert collector.get_book_genre("Оно") == "Ужасы"

    def test_get_book_genre_for_book_without_genre(self):
        collector = BooksCollector()
        collector.add_new_book("Книга без жанра")

        assert collector.get_book_genre("Книга без жанра") == ""

    def test_get_books_with_specific_genre_horror(self):
        collector = BooksCollector()
        collector.add_new_book("Оно")
        collector.set_book_genre("Оно", "Ужасы")

        assert collector.get_books_with_specific_genre("Ужасы") == ["Оно"]

    def test_get_books_genre(self):
        collector = BooksCollector()
        collector.add_new_book("Оно")
        collector.set_book_genre("Оно", "Ужасы")

        assert collector.get_books_genre() == {"Оно": "Ужасы"}

    def test_get_books_for_children_with_books_for_more_than_18yo(self):
        collector = BooksCollector()
        collector.add_new_book("Оно")
        collector.add_new_book("Шерлок")
        collector.set_book_genre("Оно", "Ужасы")
        collector.set_book_genre("Шерлок", "Детективы")

        assert collector.get_books_for_children() == []

    def test_add_book_in_favorites_when_name_is_not_in_favorites(self):
        collector = BooksCollector()
        collector.add_new_book("Оно")
        collector.add_book_in_favorites("Оно")

        assert collector.favorites == ["Оно"]

    def test_delete_book_from_favorites_multiple_books(self):
        collector = BooksCollector()
        collector.add_new_book("Звездные войны")
        collector.add_new_book("Оно")
        collector.add_book_in_favorites("Оно")
        collector.add_book_in_favorites("Звездные войны")
        collector.delete_book_from_favorites("Звездные войны")

        assert collector.favorites == ["Оно"]

    def test_get_list_of_favorites_books_list_is_empty(self):
        collector = BooksCollector()
        collector.add_new_book("Звездные войны")

        assert collector.get_list_of_favorites_books() == []

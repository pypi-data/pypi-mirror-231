import random
from readunwise.highlight import Highlight
from typing import List


def select_random_book(highlights_by_book: dict, ignored_books: List[str]) -> str:
    books = [book for book in highlights_by_book.keys() if book not in ignored_books]
    return random.choice(books)


def select_random_highlights(highlights: str, n: int) -> List[Highlight]:
    n_highlights = min(len(highlights), n)
    return random.sample(highlights, k=n_highlights)

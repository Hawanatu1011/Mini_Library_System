
# 1. Data structures (global – will be used by all functions)

books: dict[str, tuple[str, str, str, int]] = {}
members: dict[str, str] = {}
borrowed: dict[str, set[str]] = {}



# 2. Core Functions (CRUD + Borrow/Return)

def add_book(isbn: str, title: str, author: str, genre: str, total_copies: int) -> bool:
    """
    Add a book if ISBN is unique and genre is valid.
    Returns True on success, False otherwise.
    """
    valid_genres = {"Fiction", "Non-Fiction", "Sci-Fi"}
    if isbn in books:
        return False
    if genre not in valid_genres:
        return False
    if total_copies < 1:
        return False

    books[isbn] = (title, author, genre, total_copies)
    borrowed[isbn] = set()
    return True


def add_member(member_id: str, name: str) -> bool:
    """Register a new member."""
    if member_id in members:
        return False
    members[member_id] = name
    return True


def search_books(criteria: str, value: str) -> list[tuple[str, str, str, str, int]]:
    """
    Search by title, author or genre.
    Returns list of (isbn, title, author, genre, total_copies).
    """
    result = []
    lower_val = value.lower()
    for isbn, (title, author, genre, copies) in books.items():
        if criteria == "title" and lower_val in title.lower():
            result.append((isbn, title, author, genre, copies))
        elif criteria == "author" and lower_val in author.lower():
            result.append((isbn, title, author, genre, copies))
        elif criteria == "genre" and lower_val == genre.lower():
            result.append((isbn, title, author, genre, copies))
    return result


def update_book(isbn: str, **kwargs) -> bool:
    """Update any field(s) of an existing book."""
    if isbn not in books:
        return False
    title, author, genre, copies = books[isbn]
    if "title" in kwargs:
        title = kwargs["title"]
    if "author" in kwargs:
        author = kwargs["author"]
    if "genre" in kwargs:
        genre = kwargs["genre"]
    if "total_copies" in kwargs:
        copies = kwargs["total_copies"]
    books[isbn] = (title, author, genre, copies)
    return True


def delete_book(isbn: str) -> bool:
    """Delete a book only if no copies are borrowed."""
    if isbn not in books:
        return False
    if borrowed.get(isbn):
        return False
    del books[isbn]
    del borrowed[isbn]
    return True


def borrow_book(isbn: str, member_id: str) -> bool:
    """
    Borrow a copy.
    - Member must exist.
    - Book must exist.
    - At least one copy must be available.
    - Member may borrow up to 3 books.
    """
    if member_id not in members:
        return False
    if isbn not in books:
        return False

    total, = [books[isbn][3]]
    currently_borrowed = len(borrowed[isbn])
    if currently_borrowed >= total:
        return False

    # count how many books this member already has
    member_borrow_count = sum(1 for s in borrowed.values() if member_id in s)
    if member_borrow_count >= 3:
        return False

    borrowed[isbn].add(member_id)
    return True


def return_book(isbn: str, member_id: str) -> bool:
    """Return a previously borrowed copy."""
    if isbn not in borrowed or member_id not in borrowed[isbn]:
        return False
    borrowed[isbn].discard(member_id)
    if not borrowed[isbn]:
        del borrowed[isbn]
    return True
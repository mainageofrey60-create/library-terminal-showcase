"""Illustrative snippet written for this showcase (not copied from the private source).

Idea: normalise an ISBN before comparing, so '  978-X ' and '978-x' are the same book.
Also shows reading a record with defaults so a missing field does not crash the loader.
"""


def normalise_isbn(raw: str) -> str:
    return raw.strip().lower()


def is_duplicate(isbn: str, existing_isbns: list) -> bool:
    return normalise_isbn(isbn) in {normalise_isbn(i) for i in existing_isbns}


def book_from_record(record: dict) -> dict:
    """Missing fields get safe defaults instead of raising KeyError."""
    return {
        "title": record.get("title", "Unknown Title"),
        "author": record.get("author", "Unknown Author"),
        "isbn": normalise_isbn(record.get("isbn", "")),
        "borrowed": record.get("borrowed", False) is True,  # strict check, unlike bool("false")
    }


if __name__ == "__main__":
    print(is_duplicate("  ABC-123 ", ["abc-123"]))   # True
    print(book_from_record({"title": "Sample"}))

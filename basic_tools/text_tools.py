def is_palindrome(text: str) -> bool:
    """Return True if ``text`` reads the same forwards and backwards.

    Non-alphanumeric characters are ignored and comparison is case-insensitive.
    """
    normalized = ''.join(ch.lower() for ch in text if ch.isalnum())
    return normalized == normalized[::-1]


def word_count(text: str) -> int:
    """Return the number of words in ``text``."""
    return len(text.split())

from basic_tools import text_tools


def test_is_palindrome_true():
    assert text_tools.is_palindrome('A man, a plan, a canal: Panama')


def test_is_palindrome_false():
    assert not text_tools.is_palindrome('hello world')


def test_word_count():
    assert text_tools.word_count('hello world from pytest') == 4

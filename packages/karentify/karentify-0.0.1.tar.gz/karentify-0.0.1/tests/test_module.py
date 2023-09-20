import pytest  # noqa: F401

from karentify import karentify


def test_karentify():
    karentify.tiktok = False
    assert karentify('I want to buy a damburger') == 'I WaNt tO BuY A DaMbUrGeR'
    karentify.tiktok = False
    assert karentify('i want to buy a damburger') == 'i wAnT To bUy a dAmBuRgEr'

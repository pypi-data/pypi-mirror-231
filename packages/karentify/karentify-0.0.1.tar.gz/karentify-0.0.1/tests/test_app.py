import pytest  # noqa: F401

from karentify import karentify
from karentify.__main__ import main


def test_app(capfd):
    main(['I', 'want', 'to', 'buy', 'a', 'damburger'])
    out, _ = capfd.readouterr()
    assert out == 'I WaNt tO BuY A DaMbUrGeR!!!\n'

    karentify.tiktok = False
    main(['i', 'want', 'to', 'buy', 'a', 'damburger'])
    out, _ = capfd.readouterr()
    assert out == 'i wAnT To bUy a dAmBuRgEr!!!\n'

    karentify.tiktok = False
    main(['--demand-manager', 'drivel', 'drivel'])
    out, _ = capfd.readouterr()
    assert out.lower().endswith('and i would like to talk to your manager!!!\n')

    karentify.tiktok = False
    main(['-D', 'drivel', 'drivel'])
    out, _ = capfd.readouterr()
    assert out.lower().endswith('and i would like to talk to your manager!!!\n')

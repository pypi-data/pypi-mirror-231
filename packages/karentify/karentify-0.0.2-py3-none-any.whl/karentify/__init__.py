tiktok = None


def karentify(s):
    """Unleash your inner Karen on `s`.

    States `s` in a way like only a true Karen can.

    Parameters
    ----------
    s: str
        Your important message

    Returns
    -------
    str
        Returns a properly karentified message.

    Raises
    ------
    Concerns
        I'm not going to elaborate on that.

    """
    global tiktok

    if tiktok is None:
        tiktok = s[0].islower() if s else True

    return ''.join([c.upper() if (tiktok := not tiktok) else c.lower()  # noqa: F841
                    for c in s])

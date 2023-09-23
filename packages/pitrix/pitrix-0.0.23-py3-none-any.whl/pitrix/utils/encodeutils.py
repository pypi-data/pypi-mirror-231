import sys
from typing import Text


def safe_decode(text: Text, incoming=None, errors='strict'):
    if not isinstance(text, (str, bytes)):
        raise TypeError("%s can't be decoded" % type(text))

    if isinstance(text, str):
        return text

    if not incoming:
        incoming = (getattr(sys.stdin, 'encoding', None) or
                    sys.getdefaultencoding())

    try:
        return text.decode(incoming, errors)
    except UnicodeDecodeError:
        return text.decode('utf-8', errors)


def safe_encode(text: Text, incoming=None,encoding='utf-8', errors='strict'):
    if not isinstance(text, (str, bytes)):
        raise TypeError("%s can't be encoded" % type(text))

    if not incoming:
        incoming = (getattr(sys.stdin, 'encoding', None) or
                    sys.getdefaultencoding())

    if hasattr(incoming, 'lower'):
        incoming = incoming.lower()
    if hasattr(encoding, 'lower'):
        encoding = encoding.lower()

    if isinstance(text, str):
        return text.encode(encoding, errors)
    elif text and encoding != incoming:
        text = safe_decode(text, incoming, errors)
        return text.encode(encoding, errors)
    else:
        return text


def to_utf8(text: Text):
    if isinstance(text, bytes):
        return text
    elif isinstance(text, str):
        return text.encode('utf-8')
    else:
        raise TypeError("bytes or Unicode expected, got %s"% type(text).__name__)
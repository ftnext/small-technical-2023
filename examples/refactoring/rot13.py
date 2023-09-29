def transform(input: str) -> str:
    result = ""
    for character in input:
        char_code = ord(character)
        result += transform_letter(char_code)
    return result


def transform_letter(char_code: int) -> str:
    """
    >>> a_code = ord("a")
    >>> transform_letter(a_code)
    'n'
    """
    if is_between(char_code, "a", "m") or is_between(char_code, "A", "M"):
        char_code += 13
    elif is_between(char_code, "n", "z") or is_between(char_code, "N", "Z"):
        char_code -= 13
    return chr(char_code)


def is_between(char_code: int, first_letter: str, last_letter: str) -> bool:
    """
    >>> b_code = ord("b")
    >>> is_between(b_code, "a", "c")
    True
    >>> is_between(b_code, "c", "e")
    False
    >>> # 境界は含む
    >>> is_between(b_code, "b", "d")
    True
    >>> is_between(b_code, "a", "b")
    True
    """
    return code_for(first_letter) <= char_code <= code_for(last_letter)


def code_for(letter: str) -> int:
    """
    >>> code_for("a")
    97
    """
    return ord(letter)

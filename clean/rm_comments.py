"""Removing the comments from the sql code"""


def char_is_quote(char: str) -> bool:
    """
    Checks if the given character is a single quote <'>

    Args:
        char (str): A single character

    Returns:
        bool: True if the character is a single quote, False otherwise
    """
    return char == "'"


def next_char_is_quote(
        code_len: int,
        sql_code: str, ix: int
        ) -> bool:
    """
    Checks if the next character in the SQL code,
    starting from the given index, is a single quote <'>
    Two quotes indicates the escaping of the quote
    like in the string: <'John''s'>

    Args:
        l (int): The length of the SQL code string
        sql_code (str): The SQL code string
        ix (int): The current index position in the string

    Returns:
        bool: True if the next character exists and is a single quote,
            False otherwise
    """
    if ix + 1 < code_len and sql_code[ix + 1] == "'":
        return True
    return False


def is_new_line(char: str) -> bool:
    """
    Checks if the char represents newline

    Args:
        char (str): A single character

    Returns:
        bool: True if the character is a newline, False otherwise
    """
    return char in '\n\r\f\v\u2028\u2029'


def char_is_dash(char: str) -> bool:
    """
    Checks if the given character is a dash <->

    Args:
        char (str): A single character

    Returns:
        bool: True if the character is a dash, False otherwise
    """
    return char == "-"


def next_char_is_dash(
        code_len: int,
        sql_code: str,
        ix: int) -> bool:
    """
    Checks if the next character in the SQL code,
    starting from the given index, is a dash <->.
    The second dash is used to detect the beginning of a one-line comment <-->

    Args:
        l (int): The length of the SQL code string
        sql_code (str): The SQL code string
        ix (int): The current index position in the string.

    Returns:
        bool: True if the next character exists and is a dash, False otherwise
    """
    if ix + 1 < code_len and sql_code[ix + 1] == "-":
        return True
    return False


def rm_oneliners(sql_code: str) -> str:
    """
    Removes one-line comments from the sql code

    Args:
        sql_code (str): The SQL code in which we remove the one-line comments

    Returns:
        str: Cleaned SQL code without one-liners
    """

    result = ''

    is_in_quote = False
    is_in_comment = False
    is_in_escape = False

    code_len = len(sql_code)

    for ix, char in enumerate(sql_code):
        if is_new_line(char) and not is_in_quote:
            result += char
            is_in_comment = False
            continue
        if is_in_comment:
            continue
        if char_is_dash(char
                        ) and next_char_is_dash(code_len, sql_code, ix
                                                ) and not is_in_quote:
            is_in_comment = True
            continue
        if is_in_escape:
            is_in_escape = False
            result += char
            continue
        if char_is_quote(char
                         ) and next_char_is_quote(code_len, sql_code, ix):
            is_in_escape = True
            result += char
            continue
        if char_is_quote(char):
            if is_in_quote:
                is_in_quote = False
            else:
                is_in_quote = True
            result += char
            continue
        if is_in_quote:
            result += char
            continue

        result += char

    return result

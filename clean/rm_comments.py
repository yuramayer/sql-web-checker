"""Removing the comments from the sql code"""

import re


def divide_by_quotes(sql_code: str) -> list:
    """
    Splits the sql-code text by the quotes and returns the list with the elements
    
    The splitting goes with the PostgreSQL quotes <'>, but doesn't affect the <''> element. 
    The quotes <'> shouldn't be dropped, they're returning into the next element after appearing. 
    The returning list shouldn't include any empty elements as "".

    EG: divide_by_quotes("SELECT 'John''s data', column FROM table WHERE name = 'O''Reilly'")
        will return the list: ["SELECT ", "'John''s data'", 
                                ", column FROM table WHERE name = ", "'O''Reilly'"]
    
    Args: 
        sql_code (str): The PostgreSQL code that should be divided

    Returns:
        list: The elems of the sql_code string divided by <'> quote 
    """
    pattern = re.compile(r"('(?:''|[^'])*')")
    parts = pattern.split(sql_code)
    return [elem for elem in parts if elem != ""]


def rm_oneliners(sql_code: str) -> str:
    """Removes one-line comments from the sql code"""

    # re-pattern will divide      
    code_parts = divide_by_quotes(sql_code)
    new_parts = []

    for i, part in enumerate(code_parts):
        # If the text in quotes, we add it without any cleaning
        if i % 2 == 1:
            new_parts.append(part)
        else:
            # --.* re-flag will clean the comment to the new line, 
            #       so the code shouldn't be corrupted  
            cleaned = re.sub(r'--.*', '', part)
            new_parts.append(cleaned)
    return ''.join(new_parts)

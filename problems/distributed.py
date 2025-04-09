import pandas as pd
import re


def is_create_table(text):
    pattern = r"(?i)\bcreate\s+(?:\S+\s+)?table\b"
    match = re.search(pattern, text, re.IGNORECASE)
    if match:
        return True


def no_distributed(string):
    return 'distributed' not in string


def get_without_distributed(lst):
    error_lst = []
    for element in lst:
        if is_create_table(element):
            if no_distributed(element):
                error_lst.append(element)
    return error_lst


import pandas as pd
import re
from ..constants import STAGE_SCHEMA


def check_wrong_stage(sql_code_lst):
    pass


def is_create_table(text):
    pattern = r"(?i)\bcreate\s+(?:\S+\s+)?table\b"
    
    match = re.search(pattern, text, re.IGNORECASE)

    if match:
        return True
    

def get_path(text):
    pattern = r'(\b\w+\.\w+|\b\w+)\s*(?=\(|AS)'
    match = re.search(pattern, text, re.IGNORECASE)
    if match:
        return match.group(1)


def is_wrong_schema(path):
    if '.' not in path:
        return
    schema = path.split('.')[0]
    if schema != STAGE_SCHEMA:
        return True


def get_wrong_stages(lst):
    error_lst = []
    for element in lst:
        if is_create_table(element):
            path = get_path(element)
            if is_wrong_schema(path):
                error_lst.append(element)
    return error_lst


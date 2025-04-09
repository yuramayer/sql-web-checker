import pandas as pd


def check_temp(sql_code_lst):
    temps = get_temp_tables(sql_code_lst)

    temps_df = pd.DataFrame(
        {
            'error_type': ['Используются temp - таблицы'] * len(temps),
            'sql_code': temps
        }
    )
    return temps_df


def has_temp(string):
    return any([ temp_word in string 
                for temp_word in (' temp ', ' temporary ') ])


def get_temp_tables(lst):
    error_lst = []
    for element in lst:
        if has_temp(element):
            error_lst.append(element)
    return error_lst

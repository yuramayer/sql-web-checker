"""Final Dataframe module - unite the dataframe to the web page"""

import pandas as pd
from .problems import get_wrong_stages, \
    get_temp_tables, get_without_distributed


FUNCTIONS = (
    get_without_distributed,
    get_wrong_stages,
    get_temp_tables
)


def get_final_df(input_text: str) -> pd.DataFrame:
    """Process the text & return the final dataframe"""

    input_lst = input_text.lower().split(';')

    dataframes = [func(input_lst) for func in FUNCTIONS]
    assert type(dataframes) == pd.DataFrame
    res_df = pd.concat(dataframes, ignore_index=True)
    res_df.replace('\r\n', '<br>', regex=True, inplace=True)
    res_df.replace('\n', '<br>', regex=True, inplace=True)
    res_df.replace('\t', '  ', regex=True, inplace=True)
    res_df.columns = ('Error Type', 'SQL Code')

    return res_df

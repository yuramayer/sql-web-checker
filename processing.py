"""Module for the processing of the code"""

import pandas as pd


def check_code(sql_code: str) -> pd.DataFrame:
    """Checking the code for the errors"""

    print(f'The length of the code: {len(sql_code)}')

    return pd.DataFrame([[1, 2, 3], ['a', 'b', 'c']], columns=[1, 2, 3])

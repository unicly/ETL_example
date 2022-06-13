import pandas as pd
import numpy as np
from dateutil import parser
import re


def convert_date_format(input_string: str) -> str:
    """Converts a date, that is received in different formats,
        to a predefined format and returns it as a string.

    Parameters:
        input_string(str): Date as string

    Returns:
        date_obj(str): Date as string
    """

    date_obj = parser.parse(input_string)

    return date_obj.strftime("%d/%m/%Y")


def remove_na(df: pd.DataFrame) -> pd.DataFrame:
    df.dropna(axis=0, how="any", thresh=None, subset=None, inplace=True)
    return df


def remove_empty_spaces(df: pd.DataFrame) -> pd.DataFrame:
    df.replace(r"^\s*$", np.nan, regex=True, inplace=True)
    return df


def remove_ascii_chars(input_string: str) -> str:
    """The RegExp deals with ASCII characters like \\x32"""
    cleaned = re.sub(r"\\x[0-9A-Fa-f]{2}", "", input_string)
    return cleaned


def concatenate_dataframes(dataframes: list) -> pd.DataFrame:
    concatenated = pd.concat(dataframes, ignore_index=True)
    return concatenated

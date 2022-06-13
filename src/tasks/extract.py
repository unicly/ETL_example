import logging
import pandas as pd
import os
from src.exceptions import InvalidFileTypeException


def read_file(file_name: str) -> pd.DataFrame:
    """Reads files with .csv or .json extensions, otherwise throws an exception

    Parameters:
        file_name(str): File name as string

    Returns:
        pd.DataFrame(df): Content from the file as datafame
    """

    file_extension = os.path.splitext(file_name)[1]

    try:
        if file_extension == ".csv":
            return pd.read_csv(file_name, encoding="utf-8")
        elif file_extension == ".json":
            return pd.read_json(file_name, encoding="utf-8")
        else:
            raise InvalidFileTypeException
    except InvalidFileTypeException as e:
        logging.exception(f"The file format {file_extension} is not supported. {e}")
        raise

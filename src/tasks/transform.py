import logging
from iniconfig import ParseError
import pandas as pd
import src.utils as utils
import json


def clean_data(df: pd.DataFrame, publication_type: str) -> pd.DataFrame:
    """Cleans the data by removing empty records, NA's and converts date formats

    Parameters:
        de(df): Dataframe that is cleaned
        drugs_df(df): Dataframe that has been cleaned

    Returns:
        output(dict): The final output constructed from the two input dataframes
    """

    if publication_type == "pubmed":
        df["publication_type"] = "pubmed"

        # Loading from JSON converts date string to format 2020-01-01 00:00:00
        # Removing the timestamp
        df["date"] = df["date"].astype(str).str[:10]

    if publication_type == "trial":
        df["publication_type"] = "trial"
        df.rename(columns={"scientific_title": "title"}, inplace=True)

    # Replace empty records (contatining one or more spaces) with NA
    df = utils.remove_empty_spaces(df)
    df = utils.remove_na(df)

    try:
        df["date"] = df["date"].apply(utils.convert_date_format)
    except ParseError as e:
        logging.exception(f"Incorrect date format {df['date']}. {e}", exc_info=True)
        raise

    df["journal"] = df["journal"].apply(lambda x: utils.remove_ascii_chars(x))
    df["title"] = df["title"].apply(lambda x: utils.remove_ascii_chars(x))

    return df


def construct_output_data_to_json(
    all_publications_df: pd.DataFrame, drugs_df: pd.DataFrame
) -> json:
    """Contructs a dictionary in the format that shows the relations between the drugs
        and the publications.

    Parameters:
        all_publications_df(df): Dataframe that contain all publications
        drugs_df(df): Dataframe that contains a list of drugs

    Returns:
        output(dict): The final output constructed from the two input dataframes
    """

    output = []
    json_object = {}

    for drug in drugs_df["drug"]:
        if all_publications_df["title"].str.contains(drug, case=False).any():
            json_object = {"drug": drug}
            publications = all_publications_df[
                all_publications_df["title"].str.contains(drug, case=False)
            ]  # Returnernar en dataframe
            publications = publications[["date", "journal", "title", "publication_type"]]
            publications = publications.to_dict(orient="records")
            json_object.update({"publications": publications})
            output.append(json_object)

    output = json.dumps(output, indent=4, ensure_ascii=False)

    return output

import pandas as pd
from src.tasks.transform import construct_output_data_to_json
from src.tasks.transform import clean_data


def construct_output_data_to_json_for_df():
    publications = {
        "id": 2,
        "title": [
            "An evaluation of benadryl, pyribenzamine, and other so-called \
            diphenhydramine antihistaminic drugs in the treatment of allergy."
        ],
        "date": "01/01/2019",
        "journal": "Journal of emergency nursing",
        "publication_type": "pubmed",
    }

    drugs = {
        "atccode": {
            1: "S03AA",
            2: "V03AB",
            3: "A03BA",
            4: "A01AD",
            5: "6302001",
            6: "R01AD",
        },
        "drug": {
            1: "TETRACYCLINE",
            2: "ETHANOL",
            3: "ATROPINE",
            4: "EPINEPHRINE",
            5: "ISOPRENALINE",
            6: "BETAMETHASONE",
        },
    }

    publications_df = pd.DataFrame(publications)
    drugs_df = pd.DataFrame(drugs)

    result_df = construct_output_data_to_json(publications_df, drugs_df)

    assert isinstance(result_df, pd.DataFrame) is True


def test_clean_data_for_df():

    publications = {
        "id": 2,
        "title": [
            "An evaluation of benadryl, pyribenzamine, and other so-called \
            diphenhydramine antihistaminic drugs in the treatment of allergy."
        ],
        "date": "01/01/2019",
        "journal": "Journal of emergency nursing",
        "publication_type": "pubmed",
    }

    publications_df = pd.DataFrame(publications)
    result_df = clean_data(publications_df, "pubmed")

    assert isinstance(result_df, pd.DataFrame) is True

# Pipeline for publications

## Task 1: Data pipeline for publications

### Specifications

The output of the data pipeline should be a JSON file representing a link graph between the different drugs and their respective mentions in the different PubMed publications, the different scientific publications and finally the journals with the date associated with each of these mentions.

### Management rules:
- A drug is considered to be mentioned in a PubMed article or a clinical trial if it is mentioned in the title of the publication.

- A drug is considered to be mentioned by a journal if it is mentioned in a publication issued by that journal.

## Input

Input sources are CSV and JSON files that contain publications from PubMed publications and clinical trials.

## Output

The pipeline produces a JSON file that represents a link graph between the various drugs and their respective mentions in the various PubMed publications, the various scientific publications and finally the journals with the date associated with each of these mentions.

### JSON format
The format chosen to represent the graph is shown below.

```
[
    {
        "drug": "DIPHENHYDRAMINE",
        "publications": [
            {
                "date": "2020-02-01",
                "journal": "Journal of emergency nursing",
                "title": "A 44-year-old man with erythema of the face diphenhydramine, neck, and chest, weakness, and palpitations",
                "publication_type": "pubmed"
            },
            {
                "date": "2020-02-01",
                "journal": "Journal of emergency nursing",
                "title": "An evaluation of benadryl, pyribenzamine, and other so-called diphenhydramine antihistaminic drugs in the treatment of allergy.",
                "publication_type": "pubmed"
            },
        ]
    },
    {
        "drug": "ETHANOL",
        "publications": [
            {
                "date": "2020-02-01",
                "journal": "Psychopharmacology",
                "title": "Rapid reacquisition of contextual fear following extinction in mice: effects of amount of extinction, tetracycline acute ethanol withdrawal, and ethanol intoxication.",
                "publication_type": "pubmed"
            }
        ]
    },
]

```

## How to run the application

```
python main.py
```

## Task 2: Ad-Hoc

### Specifications

Set up (outside the data pipeline, you can consider it as an annex) a feature to answers the following problem:

- Extract from the json produced by the data pipeline the name of the journal that mentions the most different drugs?

### Description

Since this task is outside the pipeline it has been created in a notebook, which can be found [here](notebooks/ad-hoc.ipynb).

## Task 3: SQL

The SQL questions have been answered in the notebook [here](notebooks/sql.ipynb).

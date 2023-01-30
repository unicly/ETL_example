
import src.tasks.transform as transform
import src.tasks.extract as extract
import src.tasks.load as load
import src.utils as utils

import src.logging as log
import logging

from dotenv import dotenv_values


# Set up the Google Cloud Logging python client library
# import google.cloud.logging
# client = google.cloud.logging.Client()
# client.setup_logging()


def main():

    # EXTRACT
    # Read the files. Stop the execution if a file is missing.
    try:
        pubmed_csv_df = extract.read_file(config["SOURCE_FILE_PUBMED"])
        pubmed_json_df = extract.read_file(config["SOURCE_FILE_JOURNALS"])
        trials_df = extract.read_file(config["SOURCE_FILE_TRIALS"])
        drugs_df = extract.read_file(config["SOURCE_FILE_DRUGS"])
    except FileNotFoundError as e:
        logging.exception(
            f"A required file is missing. Stopping the application. \n{e}",
            exc_info=False,
        )
        raise

    # TRANSFORM
    pubmed_csv_df = transform.clean_data(pubmed_csv_df, "pubmed")
    pubmed_json_df = transform.clean_data(pubmed_json_df, "pubmed")
    trials_df = transform.clean_data(trials_df, "trial")

    # Merge the publication dataframes into a single dataframe
    all_publications_df = utils.concatenate_dataframes([pubmed_csv_df, trials_df, pubmed_json_df])
    all_publications_df.reset_index(drop=True, inplace=True)

    # Construct the output data
    output_json = transform.construct_output_data_to_json(all_publications_df, drugs_df)

    # LOAD
    # Write to destination
    load.write_file(output_json, config["OUTPUT_FILE"])


if __name__ == "__main__":
    # Import config variables
    config = dotenv_values(".env")

    log.setup_logging()
    main()

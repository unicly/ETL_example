import json
import logging


def write_file(json_object: json, destination: str):
    """Write a json object to a file. Overwrites the existing file if the file exists."""
    try:
        with open(destination, "w+", encoding="utf-8") as f:
            f.write(json_object)
    except IOError as e:
        logging.exception(f"The output file {destination} can't be opened for writing. {e}")

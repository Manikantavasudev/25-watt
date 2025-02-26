import os
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')


def check_file_exists(file_path):
    """
    Check if a file exists at the given path and log the steps.

    :param file_path: Path to the file to check.
    :return: True if the file exists, False otherwise.
    """
    logging.info(f"Checking if file exists: {file_path}")

    if os.path.exists(file_path):
        logging.info(f"File found: {file_path}")
        return True
    else:
        logging.error(f"File not found: {file_path}")
        return False
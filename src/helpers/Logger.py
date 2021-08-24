import csv
import coloredlogs
import logging
import os
import datetime
from typing import List
coloredlogs.install()


class Logger:
    """
    Logger can be used to log data in a standardized fashion
    """

    @staticmethod
    def log_info(text) -> None:
        logging.info(text)

    @staticmethod
    def log_warning(text) -> None:
        logging.warning(text)

    @staticmethod
    def log_error(text) -> None:
        logging.error(text)

    @staticmethod
    def save_activity(row : List, db="phonemes.csv") -> None:

        # add timestamp
        now = datetime.datetime.now()
        row = [now.strftime("%Y-%m-%d %H:%M:%S")] + row

        folder = os.path.join(os.getcwd(), "Logging")
        fp = os.path.join(folder, db)
        if os.path.exists(folder):
            if os.path.exists(fp):
                with open(fp, "a") as f:
                    csv.writer(f).writerow(row)
            else:
                with open(fp, "w") as f:
                    csv.writer(f).writerow(row)
        else:
            os.mkdir(folder)
            with open(fp, "w") as f:
                csv.writer(f).writerow(row)

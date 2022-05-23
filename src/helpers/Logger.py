import logging
import os
import coloredlogs
import traceback
import time

coloredlogs.install()


class Logger:
    """
    Logger can be used to log data in a standardized fashion
    """

    LOG_FOLDER = os.path.join(os.getcwd(), "sleeve_exception_logs")


    @staticmethod
    def log_info(text) -> None:
        logging.info(text)

    @staticmethod
    def log_warning(text) -> None:
        logging.warning(text)

    @staticmethod
    def log_error(text) -> None:
        logging.error(text)

    # Store an exception in a file with its exception, message and traceback
    @staticmethod
    def log_exception(exception: Exception):
        """
        Store an exception in a file with its exception type, message and traceback.
        @param exception              The exception to be stored.
        @param exception_type         The type of the exception.
        @param message                The message of the exception.
        @param traceback              The traceback of the exception.
        """
        # Create file path as date and time + exception type
        Logger.log_error("Logged exception: {}".format(exception))
        file_path = os.path.join(
            Logger.LOG_FOLDER,
            time.strftime("%Y-%m-%d_%H-%M-%S") + "_" + str(type(exception).__name__) + ".txt"
        )

        # Create file if it does not exist
        if not os.path.exists(Logger.LOG_FOLDER):
            os.makedirs(Logger.LOG_FOLDER)

        # Write to file
        with open(file_path, "w") as file:
            file.write("Exception: {}\n".format(exception))
            file.write("Message: {}\n".format(exception.args[0]))
            file.write("Traceback: {}\n".format(traceback.format_exc()))
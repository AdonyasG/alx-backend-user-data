#!/usr/bin/env python3
"""filtered_logger"""
from typing import List
import re
import logging
import os
import mysql.connector


PII_FIELDS = ('name', 'email', 'phone_number', 'address', 'credit_card_number')


def filter_datum(fields: List[str], redaction: str,
                 message: str, separator: str) -> str:
    """matches certain field and changes the value"""
    for field in fields:
        pattern = fr"(?<=\b{field}=)[^{separator}]+"
        message = re.sub(pattern, f"{redaction}", message)
    return message


def get_logger() -> logging.Logger:
    """new logger for a user data"""
    logger = logging.getLogger("user_data")
    logger.setLevel(logging.INFO)
    logger.propagate = False
    stream_handler = logging.StreamHandler()
    formatter = RedactingFormatter(PII_FIELDS)
    stream_handler.setFormatter(formatter)
    logger.addHandler(stream_handler)
    return logger


def get_db() -> mysql.connector.connection.MySQLConnection:
    """get_db and connect"""
    usrname = os.getenv('PERSONAL_DATA_DB_USERNAME', 'root')
    pswd = os.getenv('PERSONAL_DATA_DB_PASSWORD', 'root')
    host = os.getenv('PERSONAL_DATA_DB_HOST', 'localhost')
    database = os.getenv('PERSONAL_DATA_DB_NAME')
    return mysql.connector.connect(user=usrname, password=pswd,
                                   host=host, database=database)


class RedactingFormatter(logging.Formatter):
    """ Redacting Formatter class
        """

    REDACTION = "***"
    FORMAT = "[HOLBERTON] %(name)s %(levelname)s %(asctime)-15s: %(message)s"
    SEPARATOR = ";"

    def __init__(self, fields: List[str]):
        self.fields = fields
        super(RedactingFormatter, self).__init__(self.FORMAT)

    def format(self, record: logging.LogRecord) -> str:
        """format for logger"""
        result = filter_datum(self.fields, self.REDACTION,
                              super().format(record), self.SEPARATOR)
        return result

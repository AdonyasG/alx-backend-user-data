#!/usr/bin/env python3
"""filtered_logger"""
from typing import List
import re
import logging


def filter_datum(fields: List[str], redaction: str,
                 message: str, separator: str) -> str:
    """matches certain field and changes the value"""
    for field in fields:
        pattern = fr"(?<=\b{field}=)[^{separator}]+"
        message = re.sub(pattern, f"{redaction}", message)
    return message


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

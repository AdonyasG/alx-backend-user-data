#!/usr/bin/env python3
"""filtered_logger"""

import re


def filter_datum(fields, redaction, message, separator):
    """matches certain field and changes the value"""
    for field in fields:
        pattern = r"(?<=\b{}=)[^{}]+".format(field, separator)
        result = re.sub(pattern, f"{redaction}", message)
    return result

#!/usr/bin/env python3
"""filtered_logger"""
from typing import List
import re


def filter_datum(fields: List[str], redaction: str,
                 message: str, separator: str) -> str:
    """matches certain field and changes the value"""
    for field in fields:
        pattern = fr"(?<=\b{field}=)[^{separator}]+"
        message = re.sub(pattern, f"{redaction}", message)
    return message

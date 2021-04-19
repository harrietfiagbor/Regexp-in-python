"""
Validation Exercises

These functions return ``True`` or ``False`` depending on whether the
string passes a condition.

"""
import re

def has_vowel(string):
    # Str1 = any(k in string for k in 'aeiou') ----can be used for normal search in python
    Str1 = re.search(r'[aeiou]', string)
    return bool(Str1)
    """Return True iff the string contains one or more vowels."""


def is_integer(string):
    Str2 = re.search(r'^-?\d+$', string)
    return bool(Str2)
    """Return True iff the string represents a valid integer."""


def is_fraction(string):
    Str3 = re.search(r'^-?\d\D\d+$', string)
    return bool(Str3)
    """Return True iff the string represents a valid fraction."""


def is_valid_date(string):
    Str4 = re.search(r'\d{2}-\d{2}-\d{4}', string)
    return bool(Str4)
    """Return True iff the string represents a valid YYYY-MM-DD date."""


def is_number(string):
    Str5 = re.search(r'^-?\D?\d+\D?\d+$', string)
    return bool(Str5)
    """Return True iff the string represents a decimal number."""


def is_hex_color(string):
    Str6 = re.search(r'^#([A-Fa-f0-9]{3}|[A-Fa-f0-9]{6})$', string)
    return bool(Str6)
    """Return True iff the string represents an RGB hex color code."""

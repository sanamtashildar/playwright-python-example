"""
Common utility functions for generating random test data
"""

import random
import string


def generate_random_word(n=8, letters_only=True, alphanumeric=False):
    """Generate a random word of specified length"""
    if letters_only:
        return ''.join(random.choices(string.ascii_letters, k=n))
    if alphanumeric:
        return ''.join(random.choices(string.ascii_letters + string.digits, k=n))
    return ''.join(random.choices(string.printable.strip(), k=n))

def generate_random_number(length=5):
    """Generate a random number of specified length"""
    return (random.randint(10**(length-1), 10**length - 1))


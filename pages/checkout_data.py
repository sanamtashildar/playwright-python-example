"""
Checkout data model with dataclass for test data generation
"""

from dataclasses import dataclass, field

from utilities.common import generate_random_number, generate_random_word


@dataclass
class CheckoutData:
    """Dataclass to hold checkout form data with random generated values"""

    first_name: str = field(default_factory=lambda: generate_random_word(5))
    last_name: str = field(default_factory=lambda: generate_random_word(5))
    postal_code: str = field(default_factory=lambda: str(generate_random_number(5)))

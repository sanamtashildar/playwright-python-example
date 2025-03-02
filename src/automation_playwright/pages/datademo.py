from dataclasses import dataclass, field
from typing import Dict
@dataclass
class MyDataClass:
    my_dict: dict = field( default_factory= lambda: {"key1": "value1", "key2": "value2"})



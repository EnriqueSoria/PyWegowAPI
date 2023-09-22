from dataclasses import asdict
from typing import Any
from typing import Type

import dacite
from api_consumer.protocols import Parser


class DataclassParser(Parser):
    def __init__(self, data_class: Type):
        self.data_class = data_class

    def to_dict(self, instance: Any) -> dict:
        try:
            return asdict(instance)
        except TypeError:
            return instance

    def to_class(self, dictionary: dict) -> Any:
        return dacite.from_dict(self.data_class, dictionary)

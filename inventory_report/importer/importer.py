from abc import ABC, abstractmethod


class Importer(ABC):
    @classmethod
    @abstractmethod
    def import_data(cls, path: str, report_type: str) -> str:
        raise NotImplementedError

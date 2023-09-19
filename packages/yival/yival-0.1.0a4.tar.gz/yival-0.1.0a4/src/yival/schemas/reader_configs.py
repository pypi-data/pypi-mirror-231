from dataclasses import asdict, dataclass
from typing import Optional


@dataclass
class BaseReaderConfig:
    """
    Base configuration class for all readers.
    """

    chunk_size: int = 100

    def asdict(self):
        return asdict(self)


@dataclass
class CSVReaderConfig(BaseReaderConfig):
    """
    Configuration specific to the CSV reader.
    """

    use_first_column_as_id: bool = False
    expected_result_column: Optional[str] = None

    def asdict(self):
        return asdict(self)

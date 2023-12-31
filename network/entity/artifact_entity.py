from dataclasses import dataclass
from typing import List


@dataclass
class DataIngestionArtifact:
    feature_store_folder_path: str
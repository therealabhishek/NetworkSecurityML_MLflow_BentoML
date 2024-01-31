from dataclasses import dataclass
from typing import List


@dataclass
class DataIngestionArtifact:
    feature_store_folder_path: str


@dataclass
class DataValidationArtifact:
    valid_data_dir: str

    invalid_data_dir: str

    training_file_path: str

    testing_file_path: str


@dataclass
class DataTransformationArtifact:
    transformed_object_file_path: str

    transformed_train_file_path: str

    transformed_test_file_path: str
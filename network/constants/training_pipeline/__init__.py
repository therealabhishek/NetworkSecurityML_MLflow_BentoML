import os
from datetime import datetime

import numpy as np


TIMESTAMP: datetime = datetime.now().strftime("%m_%d_%Y_%H_%M_%S")
PIPELINE_NAME: str = "network"
ARTIFACT_DIR:str = "artifacts"
PREPROCSSING_OBJECT_FILE_NAME: str = "preprocessing.pkl"
TARGET_COLUMN: str = "Result"


"""
    Data Ingestion Constants
"""
DATA_INGESTION_DIR_NAME: str = "data_ingestion"
DATA_INGESTION_BUCKET_NAME: str = "network-batchdata"
DATA_INGESTION_BUCKET_FOLDER_NAME: str = "data/train_batch"
DATA_INGESTION_FEATURE_STORE_DIR: str = "feature_store"

"""
    Data Validation Constants
"""
DATA_VALIDATION_DIR_NAME: str = "data_validation"
DATA_VALIDATION_TRAIN_SCHEMA: str = "config/network_schema_training.yaml"
DATA_VALIDATION_REGEX: str = "config/network_regex.txt"
DATA_VALIDATION_VALID_DIR: str = "valid"
DATA_VALIDATION_INVALID_DIR: str = "invalid"
DATA_VALIDATION_TEST_SIZE: str = 0.3
DATA_VALIDATION_TRAIN_COMPRESSED_FILE_PATH: str = "train_input_file.csv"
DATA_VALIDATION_TRAIN_FILE_PATH: str = "train.csv"
DATA_VALIDATION_TEST_FILE_PATH: str = "test.csv"


"""
    Data Transformation Constants
"""
DATA_TRANSFORMATION_DIR_NAME: str = "data_transformation"
DATA_TRANSFORMATION_TRANSFORMED_DATA_DIR: str = "transformed"
DATA_TRANSFORMATION_TRANSFORMED_OBJECT_DIR: str = "transformed_object"
DATA_TRANSFORMATION_TRAIN_FILE_PATH: str = "train.npy"
DATA_TRANSFORMATION_TEST_FILE_PATH: str = "test.npy"
DATA_TRANSFORMATION_IMPUTER_PARAMS: dict = {
    "missing_values": np.nan,
    "n_neighbors": 3,
    "weights": "uniform",
}


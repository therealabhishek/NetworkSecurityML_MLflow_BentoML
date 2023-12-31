import os
from datetime import datetime

import numpy as np


TIMESTAMP: datetime = datetime.now().strftime("%m_%d_%Y_%H_%M_%S")
PIPELINE_NAME: str = "network"
ARTIFACT_DIR:str = "artifacts"


"""
    Data Ingestion Constants
"""
DATA_INGESTION_DIR_NAME: str = "data_ingestion"
DATA_INGESTION_BUCKET_NAME: str = "network-batchdata"
DATA_INGESTION_BUCKET_FOLDER_NAME: str = "data/train_batch"
DATA_INGESTION_FEATURE_STORE_DIR: str = "feature_store"
import os
from datetime import datetime
from dataclasses import dataclass

from network.constants import training_pipeline


class TrainingPipelineConfig:
    def __init__(self, timestamp=datetime.now()):
        timestamp: datetime = timestamp.strftime("%m_%d_%Y_%H_%M_%S")

        self.pipeline_name: str = training_pipeline.PIPELINE_NAME

        self.artifact_dir: str = os.path.join(training_pipeline.ARTIFACT_DIR, timestamp)

        self.timestamp: str = timestamp


class DataIngestionConfig:
    def __init__(self, training_pipeline_config: TrainingPipelineConfig):
        self.data_ingestion_dir: str = os.path.join(
            training_pipeline_config.artifact_dir,
            training_pipeline.DATA_INGESTION_DIR_NAME
        )

        self.data_ingestion_bucket_name: str = (
            training_pipeline.DATA_INGESTION_BUCKET_NAME
        )

        self.data_ingestion_bucket_folder_name: str = (
            training_pipeline.DATA_INGESTION_BUCKET_FOLDER_NAME
        )

        self.data_ingestion_feature_store_folder_name: str = os.path.join(
            self.data_ingestion_dir, training_pipeline.DATA_INGESTION_FEATURE_STORE_DIR
        )
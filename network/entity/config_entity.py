import os
from datetime import datetime
from dataclasses import dataclass

from network.constants import training_pipeline


# Training Pipeline Config:
class TrainingPipelineConfig:
    def __init__(self, timestamp=datetime.now()):
        timestamp: datetime = timestamp.strftime("%m_%d_%Y_%H_%M_%S")

        self.pipeline_name: str = training_pipeline.PIPELINE_NAME

        self.artifact_dir: str = os.path.join(training_pipeline.ARTIFACT_DIR, timestamp)

        self.timestamp: str = timestamp


# Data Ingestion Config:
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


# Data Validation Config:
class DataValidationConfig:
    def __init__(self, training_pipeline_config: TrainingPipelineConfig):
        self.data_validation_dir: str = os.path.join(
            training_pipeline_config.artifact_dir,
            training_pipeline.DATA_VALIDATION_DIR_NAME,
        )

        self.data_validation_training_schema_path: str = (
            training_pipeline.DATA_VALIDATION_TRAIN_SCHEMA
        )

        self.data_validation_regex_path: str = training_pipeline.DATA_VALIDATION_REGEX

        self.data_validation_valid_data_dir: str = os.path.join(
            self.data_validation_dir, training_pipeline.DATA_VALIDATION_VALID_DIR
        )

        self.data_validation_invalid_data_dir: str = os.path.join(
            self.data_validation_dir, training_pipeline.DATA_VALIDATION_INVALID_DIR
        )

        self.data_validation_split_ratio: float = (
            training_pipeline.DATA_VALIDATION_TEST_SIZE
        )

        self.merged_file_path: str = os.path.join(
            self.data_validation_dir,
            training_pipeline.DATA_VALIDATION_TRAIN_COMPRESSED_FILE_PATH,
        )

        self.training_file_path: str = os.path.join(
            self.data_validation_dir,
            training_pipeline.DATA_VALIDATION_TRAIN_FILE_PATH,
        )

        self.testing_file_path: str = os.path.join(
            self.data_validation_dir,
            training_pipeline.DATA_VALIDATION_TEST_FILE_PATH,
        )


# Data Transformation Config:
class DataTransformationConfig:
    def __init__(self, training_pipeline_config: TrainingPipelineConfig):
        self.data_transformation_dir: str = os.path.join(
            training_pipeline_config.artifact_dir,
            training_pipeline.DATA_TRANSFORMATION_DIR_NAME,
        )

        self.transformed_data_dir: str = os.path.join(
            self.data_transformation_dir,
            training_pipeline.DATA_TRANSFORMATION_TRANSFORMED_DATA_DIR,
        )

        self.transformed_object_file_path: str = os.path.join(
            self.data_transformation_dir,
            training_pipeline.DATA_TRANSFORMATION_TRANSFORMED_OBJECT_DIR,
            training_pipeline.PREPROCSSING_OBJECT_FILE_NAME,
        )

        self.transformed_train_file_path: str = os.path.join(
            self.transformed_data_dir,
            training_pipeline.DATA_TRANSFORMATION_TRAIN_FILE_PATH,
        )

        self.transformed_test_file_path: str = os.path.join(
            self.transformed_data_dir,
            training_pipeline.DATA_TRANSFORMATION_TEST_FILE_PATH,
        )
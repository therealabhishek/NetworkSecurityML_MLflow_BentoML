import sys

from network.components.data_ingestion import DataIngestion
from network.components.data_validation import DataValidation

from network.entity.artifact_entity import (
    DataIngestionArtifact,
    DataValidationArtifact
)

from network.entity.config_entity import(
    TrainingPipelineConfig,
    DataIngestionConfig,
    DataValidationConfig
)

from network.exception import NetworkException



class TrainPipeline:
    is_pipeline_running = False

    def __init__(self):
        self.training_pipeline_config: TrainingPipelineConfig = TrainingPipelineConfig()
        

    def start_data_ingestion(self) -> DataIngestionArtifact:
        """
        It takes in a training pipeline config, creates a data ingestion config, creates a data ingestion
        object, and then initiates data ingestion

        Returns:
          DataIngestionArtifact
        """
        try:
            self.data_ingestion_config: DataIngestionConfig = DataIngestionConfig(
                training_pipeline_config=self.training_pipeline_config
            )

            data_ingestion: DataIngestion = DataIngestion(
                data_ingestion_config=self.data_ingestion_config
            )

            data_ingestion_artifact: DataIngestionArtifact = (
                data_ingestion.initiate_data_ingestion()
            )

            return data_ingestion_artifact

        except Exception as e:
            raise NetworkException(e, sys)
        

    def start_data_validation(
        self, data_ingestion_artifact: DataIngestionArtifact
    ) -> DataValidationArtifact:
        """
        A function that takes in a data ingestion artifact and returns a data validation artifact.

        Args:
          data_ingestion_artifact (DataIngestionArtifact): DataIngestionArtifact

        Returns:
          DataValidationArtifact
        """
        try:
            self.data_validation_config: DataValidationConfig = DataValidationConfig(
                training_pipeline_config=self.training_pipeline_config
            )

            data_validation: DataValidation = DataValidation(
                data_ingestion_artifact=data_ingestion_artifact,
                data_validation_config=self.data_validation_config,
            )

            data_validation_artifact: DataValidationArtifact = (
                data_validation.initiate_data_validation()
            )

            return data_validation_artifact

        except Exception as e:
            raise NetworkException(e, sys)
        

    def run_pipeline(self):
        try:
            TrainPipeline.is_pipeline_running = True

            data_ingestion_artifact: DataIngestionArtifact = self.start_data_ingestion()

            print("Data Ingestion Completed!")

            data_validation_artifact: DataValidationArtifact = (
                self.start_data_validation(
                    data_ingestion_artifact=data_ingestion_artifact
                )
            )

            print("Data Validation Completed!")

        except Exception as e:
            raise NetworkException(e, sys)


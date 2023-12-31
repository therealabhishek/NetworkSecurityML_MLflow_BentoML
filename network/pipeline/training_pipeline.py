import sys

from network.components.data_ingestion import DataIngestion

from network.entity.artifact_entity import (
    DataIngestionArtifact
)

from network.entity.config_entity import(
    TrainingPipelineConfig,
    DataIngestionConfig
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
        

    def run_pipeline(self):
        try:
            TrainPipeline.is_pipeline_running = True

            data_ingestion_artifact: DataIngestionArtifact = self.start_data_ingestion()

        except Exception as e:
            raise NetworkException(e, sys)


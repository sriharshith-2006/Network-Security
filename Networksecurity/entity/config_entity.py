import os
from dataclasses import dataclass
from datetime import datetime
from Networksecurity.constants.training_pipe import *
TIMESTAMP = datetime.now().strftime("%m_%d_%Y_%H_%M_%S")
@dataclass
class TrainingPipelineConfig:
    pipeline_name: str = PIPELINE_NAME
    artifact_dir: str = os.path.join(
        ARTIFACT_DIR,
        TIMESTAMP
    )
@dataclass
class DataIngestionConfig:
    training_pipeline_config: TrainingPipelineConfig
    data_ingestion_dir: str = os.path.join(
        TrainingPipelineConfig.artifact_dir,
        DATA_INGESTION_DIR
    )
    feature_store_file_path: str = os.path.join(
        data_ingestion_dir,
        RAW_DATA_FILE_NAME
    )

    training_file_path: str = os.path.join(
        data_ingestion_dir,
        TRAIN_FILE_NAME
    )

    testing_file_path: str = os.path.join(
        data_ingestion_dir,
        TEST_FILE_NAME
    )

    train_test_split_ratio: float = TRAIN_TEST_SPLIT_RATIO

    collection_name: str = COLLECTION_NAME

    database_name: str = DATABASE_NAME

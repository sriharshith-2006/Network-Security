import os
TARGET_COLUMN = "Result"
PIPELINE_NAME = "NetworkSecurity"
ARTIFACT_DIR = "artifacts"
FILE_NAME="phisingData.csv"

DATA_INGESTION_DIR = "data_ingestion"
RAW_DATA_FILE_NAME = "raw.csv"
TRAIN_FILE_NAME = "train.csv"
TEST_FILE_NAME = "test.csv"

TRAIN_TEST_SPLIT_RATIO = 0.2
RANDOM_STATE = 42

DATABASE_NAME = "Sriharshith"
COLLECTION_NAME = "NetworkData"

DATA_VALIDATION_DIR = "data_validation"
VALID_DATA_DIR = "validated"
INVALID_DATA_DIR = "invalid"


DATA_TRANSFORMATION_DIR = "data_transformation"

PREPROCESSOR_FILE_NAME = "preprocessor.pkl"



MODEL_TRAINER_DIR = "model_trainer"

MODEL_FILE_NAME = "model.pkl"

EXPECTED_ACCURACY = 0.70
MODEL_EVALUATION_DIR = "model_evaluation"
MODEL_PUSHER_DIR = "model_pusher"
SAVED_MODEL_DIR = "saved_models"
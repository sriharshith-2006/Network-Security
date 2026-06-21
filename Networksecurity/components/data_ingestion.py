from Networksecurity.exception.exception import CustomException
from Networksecurity.logging import logger
from Networksecurity.entity.config_entity import DataIngestionConfig
from Networksecurity.entity.artifcat_entity import DataIngestionArtifact
from Networksecurity.entity.config_entity import TrainingPipelineConfig
import os
import sys
import pymongo
import pandas as pd
from typing import List
from sklearn.model_selection import train_test_split
import numpy as np

from dotenv import load_dotenv
load_dotenv()
MONGO_DB_URL=os.getenv("MONGO_DB_KEY")
class DataIngestion:
    def __init__(self,data_ingestion_config:DataIngestionConfig):
        try :
            self.data_ingestion_config=data_ingestion_config
        except Exception as e:
            raise CustomException(e,sys)
    def fromdb(self):
        try:
            database=self.data_ingestion_config.database_name
            collection_name=self.data_ingestion_config.collection_name
            self.mongo_client=pymongo.MongoClient(MONGO_DB_URL)
            collection=self.mongo_client[database][collection_name]
            df=pd.DataFrame(list(collection.find()))
            if "_id" in df.columns.to_list():
                df=df.drop(columns=["_id"],axis=1)
            df.replace({"na":np.nan},inplace=True)
        except Exception as e:
            raise CustomException(e,sys)
        return df
    def feature_store(self,dataframe:pd.DataFrame):
         feature_file_path=self.data_ingestion_config.feature_store_file_path
         dir_path=os.path.dirname(feature_file_path)
         os.makedirs(dir_path,exist_ok=True)
         dataframe.to_csv(feature_file_path,index=False,header=True)
         return dataframe
    def train_test_split_data(self,dataframe:pd.DataFrame):
        try:
            train_set,test_set=train_test_split(dataframe,test_size=self.data_ingestion_config.train_test_split_ratio,random_state=42)
            dir_path1=os.path.dirname(self.data_ingestion_config.training_file_path)
            dir_path2=dir_path1=os.path.dirname(self.data_ingestion_config.testing_file_path)
            os.makedirs(dir_path1,exist_ok=True)
            os.makedirs(dir_path2,exist_ok=True)
            train_set.to_csv(self.data_ingestion_config.training_file_path,index=False,header=True)
            test_set.to_csv(self.data_ingestion_config.testing_file_path,index=False,header=True)
        except Exception as e:
            raise CustomException(e,sys)
    def intiatite(self):
        try:
            dataframe=self.fromdb() 
            dataframe=self.feature_store(dataframe)
            self.train_test_split_data(dataframe)
            artifact=DataIngestionArtifact(train_path=self.data_ingestion_config.training_file_path,
                                           test_path=self.data_ingestion_config.testing_file_path,
                                           raw_path=self.data_ingestion_config.feature_store_file_path)
        except Exception as e:
            raise CustomException(e,sys)
        return artifact
if __name__ == "__main__":
    try:
        # Create configuration object
        training_pipeline=TrainingPipelineConfig()
        data_ingestion_config = DataIngestionConfig(training_pipeline)

        # Create DataIngestion object
        data_ingestion = DataIngestion(data_ingestion_config=data_ingestion_config)

        # Run data ingestion
        artifact = data_ingestion.intiatite()

        print("Data Ingestion Completed Successfully!")
        print(artifact)

    except Exception as e:
        raise CustomException(e, sys)
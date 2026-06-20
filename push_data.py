from Networksecurity.exception.exception import CustomException
from Networksecurity.logging import logger
import pandas as pd
import os
import sys
import json
import pymongo
from dotenv import load_dotenv
load_dotenv()
MONGO_DB_URL=os.getenv('MONGO_DB_KEY')
class NetworkExtract():
    def __init__(self):
        try:
            pass
        except Exception as e:
            raise CustomException(e,sys)
        
    def csv_to_json(self,file_path):
        try:
            df=pd.read_csv(file_path)
            df.reset_index(drop=True,inplace=True)
            records=list(json.loads(df.T.to_json()).values())
            return records
        except Exception as e:
            raise CustomException(e,sys)
    def insert_to_mongo(self,records,database,collection):
        try:
            self.database=database
            self.collection=collection
            self.records=records
            self.mongo_client=pymongo.MongoClient(MONGO_DB_URL)
            self.database=self.mongo_client[self.database]
            self.collection=self.database[collection]
            self.collection.insert_many(self.records)
            return len(self.records)
        except Exception as e:
            raise CustomException(e,sys)
if __name__=='__main__':
      FILE_PATH='NetworkData\phisingData.csv'
      DATABASE='Sriharshith'
      Collection='NetworkData'
      obj=NetworkExtract()
      records=obj.cv_to_json(FILE_PATH)
      len_records=obj.insert_to_mongo(records,DATABASE,Collection)
      print(len_records)
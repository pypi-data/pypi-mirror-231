import pandas as pd
from google.oauth2 import service_account
import pandas_gbq
from google.cloud import bigquery
import os
import dataflowutil.config.extra_var as extra_v
from datetime import datetime

class UploadData:
    def __init__(self,connection,spreadsheets):
        self.cn = connection
        self.spreadsheets = spreadsheets
        self.credentials = service_account.Credentials.from_service_account_file(os.path.join(extra_v.PATH_CREDENTIALS, self.cn.credentials_path) ) # Same Credentials Storage Client

    def upload_data(self,raw_data):
        if len(raw_data) <= 0:
            print("[UploadData] Alert: 0 items found to update.")
            return
        
        for df_upload,tag,index in raw_data.values():
            try:
                #Replace DTypes and Replace all types Objects to String
                df_upload = df_upload.convert_dtypes()
                for col in df_upload.select_dtypes(include='object'):
                    df_upload[col] = df_upload[col].astype("string") 

                pandas_gbq.to_gbq(df_upload,f"{self.cn.name_db_bigquery}.{tag}", project_id=self.cn.project_id,credentials=self.credentials,if_exists="replace")
                print(f"[UploadData] Successful Upload Data: NAME_DATA: {tag} // DB_NAME: {self.cn.name_db_bigquery} // ProjectID: {self.cn.project_id}")
                self.spreadsheets.update_spreadsheets(self.cn.id_load_bucket,extra_v.NAME_SHEET,f"F{index+1}",str(datetime.now()))
                self.spreadsheets.update_spreadsheets(self.cn.id_load_bucket,extra_v.NAME_SHEET,f"E{index+1}",extra_v.STATUS_UPDATE["UPDATE"])

                
            except:
                import sys
                tipo_excepcion, valor_excepcion, traceback = sys.exc_info()
                print("Tipo de excepción:", tipo_excepcion)
                print("Valor de excepción:", valor_excepcion)
                print("Traceback:", traceback)
                print(f"[UploadData] Error Upload Data: NAME_DATA: {tag} // DB_NAME: {self.cn.name_db_bigquery} // ProjectID: {self.cn.project_id}")
        
        df_upload = None
        raw_data = None

import time
import yaml
import schedule
import datetime
import pygsheets
import pandas as pd
from dotenv import load_dotenv
load_dotenv()

with open("config.yaml") as f:
    config = yaml.safe_load(f)

initDate = datetime.today()

def detect_table_exist(
    
):
    return 

def define_new_data_table(
    county: str
):
    return 

def store_data_table(
    county: str
):
    return 

def crawl_taipei():

    rawData = pd.read_json("https://tcgbusfs.blob.core.windows.net/dotapp/youbike/v2/youbike_immediate.json")

    return

def crawl_kaohsiung():

    rawData = pd.read_json(config["Taipei_URL"])

    return

def crawl_new_taipei():

    rawData = pd.read_json(config["New_Taipei_URL"])

    return

def crawl_taoyuan():

    rawData = pd.read_json(config["Taoyuan_URL"])

    return 

totalData = list()
while True:
    rawData = pd.read_json("https://tcgbusfs.blob.core.windows.net/dotapp/youbike/v2/youbike_immediate.json")
    totalData.append(rawData)
    if str(datetime.today()).split(" ")[0] == str(initDate + timedelta(minutes = 2)).split(" ")[0]:
        totalData = pd.concat(totalData, axis = 0).drop_duplicates()
        totalData.to_excel(f"{str(datetime.today())}.xlsx", index = None)
        initDate = datetime.today()
        totalData = list()
    else:
        time.sleep(30)
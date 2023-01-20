import time
from datetime import datetime, timedelta
import pandas as pd

initDate = datetime.today()
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
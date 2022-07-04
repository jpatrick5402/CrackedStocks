import requests
import os
import time
import json
import datetime
import robin_stocks


def get_company_names(): #Gets ticker name for every U.S. company on nasdaq
    with open("../TickerList.txt", "r") as f:
        namelist = f.readlines()
    return namelist

def get_stock_info_API(company): #Gets critical stock information from Alpha Vantage API
    try:
        Key = os.environ.get("KEY")
        url = f'https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol={company}&interval=5min&apikey={Key}'
        r = requests.get(url)
        data = r.json()
        print("---Data reveived")
        return data
    except:
        print("---Using Prior Data")
        with open("PriorPrice.json", "r") as f:
            data = json.load(f)
        return data


def evaluate_API(data):
    try:
        timestr = str(datetime.date.today())
        if int(timestr[-2:]) - 1 < 10:
            yesterday = "0" + str(int(timestr[-2:])-1)
        else:
            yesterday = timestr[0:8] + str(int(timestr[-2:]) - 1)
        print(data["Time Series (5min)"][f"2022-07-{yesterday} 12:00:00"])
        print(data["Time Series (5min)"][f"2022-07-{yesterday} 16:00:00"])
        print(data["Time Series (5min)"][f"2022-07-{yesterday} 20:00:00"])
    except:
        return False

#Invest with API
def invest(dec):
    pass

def save(data):
    
    return 0

def main():
    total = get_company_names()
    for i in total:
        print("\n"+i.split(" ")[0]+"\n")
        data = get_stock_info_API(i.split(" ")[0])
        decision = evaluate_API(data)
        invest(decision)
        time.sleep(1)

if __name__ == "__main__":
    main()

import requests
import os
import time

def get_company_names(): #Gets ticker name for every U.S. company on nasdaq
    with open("../TickerList.txt", "r") as f:
        namelist = f.readlines()
    return namelist

#Scrape the web and find the company's stock data
def get_stock_info(ncompany):
    #Getting the url
    URL = "https://www.google.com/search?q={}+stock".format(ncompany)
    page = requests.get(URL)
    formatted = page.text.split("<")

    #Parsing the google webpage for the exact data
    for index in formatted:
        if "BNeawe iBp4i AP7Wnd" in index:
            h=index.split(">")
            if h[-1] != "":
                price = h[-1].replace(",","")
                price = float(price)
                break
        else:
            price = 0


    changes = []
    #Looking for more nums
    for index in formatted:
        if "UMOHqf fePwtd" in index:
            changes.append(float(index[0:-8].split(">")[-1].replace(",","")))

        if "UMOHqf JoSNhf" in index:
            changes.append(float(index[0:-8].split(">")[-1].replace(",","")))
    #Creating variables
    if len(changes) == 1:
        duringhours = changes[0]
        afterhours = 0
    elif len(changes) == 2:
        duringhours = changes[0]
        afterhours = changes[1]
    elif len(changes) == 0:
        duringhours = 0
        afterhours = 0
    else:
        duringhours = 0
        afterhours = 0

   #Checking if a variable is unspecified
    if price == "NULL" or duringhours == "NULL" or afterhours == "NULL":
        #print("ERROR: INCORECTD WEB FORMATTING")
        #print("NOTE: Try a different company.")
        pass
        
    return {"price":price,"duringhours":duringhours,"afterhours":afterhours}

def get_stock_info_API(company): #Gets critical stock information from Alpha Vantage API
    Key = os.environ.get("KEY")
    url = f'https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol={company}&interval=5min&apikey={Key}'
    r = requests.get(url)
    data = r.json()
    return data
    
#Determine to Buy or Sell
def evaluate(data):
    if data["price"] != "NULL" and data["duringhours"] != "NULL" and data["afterhours"] != "NULL":
        if data["duringhours"] + data["afterhours"] < 0:
            return "---SELL"
        elif data["duringhours"] + data["afterhours"] > 0:
            return "---BUY"
    else:
        return "---FAILURE"

#Automatically invest with API
def invest():
    pass

def main():
    total = get_company_names()
    print(total[0].split(" ")[0])
    for i in total:
        print(i.split(" ")[0])
        data = get_stock_info_API(i.split(" ")[0])
        time.sleep(1)

if __name__ == "__main__":
    main()

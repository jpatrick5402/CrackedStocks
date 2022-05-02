import requests
#import json

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



#Show detailed output
def details(data):
    print("Stock Price: {}".format(data["price"]))
    print("Price During Hours: {}".format(data["duringhours"]))
    print("Price After Hours: {}".format(data["afterhours"]))


    
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
def Auto_Invest():
    pass


if __name__ == "__main__":

    with open("file.txt", "r") as f:
        fstring = f.read()

    formedabbr = fstring.split("$")


    for index in formedabbr:
        print("Company: {}".format(index[-6:-1].split(" ")[-1]))        
        companystockinfo = get_stock_info(index[-6:-1].split(" ")[-1])
#        print(companystockinfo)
#        details(companystockinfo)
        print(evaluate(companystockinfo))




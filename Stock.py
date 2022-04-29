import requests
#import json

#Scrape the web and find the company's stock data
def get_stock_info(ncompany):
    #Getting the url
    URL = "https://www.google.com/search?q={}+stock&rlz=1C1CHBF_enUS962US962&sxsrf=ALiCzsYrFvoNHcQ6waoqxD94uasSkjPDgA%3A1651188111073&ei=jyFrYqqBBOi7ytMPqriwwAw&ved=0ahUKEwjqhMWG87f3AhXonXIEHSocDMgQ4dUDCA4&uact=5&oq=Tesla+stock&gs_lcp=Cgdnd3Mtd2l6EAMyDAgjECcQnQIQRhD6ATIECCMQJzIECCMQJzILCAAQgAQQsQMQgwEyEAgAEIAEEIcCELEDEIMBEBQyCwgAEIAEELEDEIMBMgsIABCABBCxAxCDATILCAAQgAQQsQMQgwEyCwgAEIAEELEDEIMBMgsIABCABBCxAxCDAToHCCMQsAMQJzoHCAAQRxCwAzoHCAAQsAMQQzoKCAAQ5AIQsAMYAToSCC4QxwEQowIQyAMQsAMQQxgCOhUILhDHARCjAhDUAhDIAxCwAxBDGAI6BQgAEJECOggILhCABBCxAzoOCC4QgAQQsQMQxwEQowI6BQgAEIAEOggIABCxAxCDAToHCCMQ6gIQJzoECAAQQzoKCAAQsQMQgwEQQzoTCC4QsQMQgwEQxwEQowIQ1AIQQzoLCC4QgAQQxwEQrwE6CAgAEIAEELEDOhQILhCABBCxAxCDARDHARCjAhDUAjoKCC4QxwEQowIQQzoLCC4QgAQQsQMQgwFKBAhBGABKBAhGGAFQuA1Yr0lgskxoBXABeASAAfkGiAH-J5IBDTAuOS4yLjIuMS4yLjGYAQCgAQGwAQrIARHAAQHaAQYIARABGAnaAQYIAhABGAg&sclient=gws-wiz".format(ncompany)
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
            price = "NULL"


    changes = []
    #Looking for more nums
    for index in formatted:
        if "UMOHqf fePwtd" in index:
            changes.append(float(index[0:-8].split(">")[-1].replace(",","")))

        if "UMOHqf JoSNhf" in index:
            changes.append(float(index[0:-8].split(">")[-1].replace(",","")))
    #Creating variables
    if len(changes) == 2:
        duringhours = changes[0]
        afterhours = changes[1]
    else:
        duringhours = "NULL"
        afterhours = "NULL"

#    print("Company: {}".format(ncompany))
#    print("Stock Price: {}".format(price))
#    print("Price During Hours: {}".format(duringhours))
#    print("Price After Hours: {}".format(afterhours))


    # This is where the algorithmic portion fo my code will take place
#    if duringhours + afterhours > 1:
#        print("Buy")
#    elif duringhours + afterhours < 1:
#        print("Sell")
#    else:
#        print("Pause")

    if price == "NULL" or duringhours == "NULL" or afterhours == "NULL":
        #print("ERROR: INCORECTD WEB FORMATTING")
        #print("NOTE: Try a different company.")
        pass
        
    return {"price":price,"duringhours":duringhours,"afterhours":afterhours}

#Determine to Buy or Sell
def evaluate(data):
    if data["price"] != "NULL" and data["duringhours"] != "NULL" and data["afterhours"] != "NULL":
        if data["duringhours"] + data["afterhours"] < 1:
            return "---SELL"
        elif data["duringhours"] + data["afterhours"] > 1:
            return "---BUY"
    else:
        return "---FAILURE"


if __name__ == "__main__":

    with open("file.txt", "r") as f:
        fstring = f.read()

    formedabbr = fstring.split("$")


    for index in formedabbr:
        print(index[-6:-1].split(" ")[-1])        
        companystockinfo = get_stock_info(index[-6:-1].split(" ")[-1])
#        print(companystockinfo)
        print(evaluate(companystockinfo))
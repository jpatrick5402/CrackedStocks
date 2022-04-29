import requests
import json
import math
import webbrowser as wb

#Getting the url
company = ""
URL = "https://www.google.com/search?q=Tesla+stock&rlz=1C1CHBF_enUS962US962&sxsrf=ALiCzsYrFvoNHcQ6waoqxD94uasSkjPDgA%3A1651188111073&ei=jyFrYqqBBOi7ytMPqriwwAw&ved=0ahUKEwjqhMWG87f3AhXonXIEHSocDMgQ4dUDCA4&uact=5&oq=Tesla+stock&gs_lcp=Cgdnd3Mtd2l6EAMyDAgjECcQnQIQRhD6ATIECCMQJzIECCMQJzILCAAQgAQQsQMQgwEyEAgAEIAEEIcCELEDEIMBEBQyCwgAEIAEELEDEIMBMgsIABCABBCxAxCDATILCAAQgAQQsQMQgwEyCwgAEIAEELEDEIMBMgsIABCABBCxAxCDAToHCCMQsAMQJzoHCAAQRxCwAzoHCAAQsAMQQzoKCAAQ5AIQsAMYAToSCC4QxwEQowIQyAMQsAMQQxgCOhUILhDHARCjAhDUAhDIAxCwAxBDGAI6BQgAEJECOggILhCABBCxAzoOCC4QgAQQsQMQxwEQowI6BQgAEIAEOggIABCxAxCDAToHCCMQ6gIQJzoECAAQQzoKCAAQsQMQgwEQQzoTCC4QsQMQgwEQxwEQowIQ1AIQQzoLCC4QgAQQxwEQrwE6CAgAEIAEELEDOhQILhCABBCxAxCDARDHARCjAhDUAjoKCC4QxwEQowIQQzoLCC4QgAQQsQMQgwFKBAhBGABKBAhGGAFQuA1Yr0lgskxoBXABeASAAfkGiAH-J5IBDTAuOS4yLjIuMS4yLjGYAQCgAQGwAQrIARHAAQHaAQYIARABGAnaAQYIAhABGAg&sclient=gws-wiz"
page = requests.get(URL)
formatted = page.text.split("<")

#Parsing the google webpage for the exact data
for index in formatted:
    if "BNeawe iBp4i AP7Wnd" in index:
        h=index.split(">")
        if h[-1] != "":
            price = h[-1].strip()
            price = float(price)

changes = []

for index in formatted:
    if "UMOHqf fePwtd" in index:
        try:
            changes.append(float(index[0:-8].split(">")[-1]))
        except:
            duringhours = 0
    if "UMOHqf JoSNhf" in index:
        try:
            changes.append(float(index[0:-8].split(">")[-1]))
        except:
            afterhours = 0
#Using the data to make a descision
duringhours = changes[0]
afterhours = changes[1]

print("Stock Price: {}".format(price))
print("Price".format(duringhours))
print(afterhours)


# This is where the algorithmic portion fo my code will take place
if duringhours + afterhours > 1:
    print("Buy")
elif duringhours + afterhours < 1:
    print("Sell")
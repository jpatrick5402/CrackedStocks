#import string
#from xml.sax import xmlreader
import requests
import json
import math
company = "Microsoft"
URL = "https://www.google.com/search?q={company}+stocks"
page = requests.get(URL)

formatted = page.text.split("<")

for index in formatted:
    if "BNeawe iBp4i AP7Wnd" in index:
        h=index.split(">")
        if h[-1] != "":
            print(h[-1].strip())
            price = h[-1].strip()

for index in formatted:
    if "UMOHqf fePwtd" in index:
        print(index[0:-8].split(">")[-1])
    if "today" in index:
        print(index)

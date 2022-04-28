#import string
#from xml.sax import xmlreader
import requests
import json

URL = "https://www.google.com/search?q=microsoft+stock+price+5+days&rlz=1C1CHBF_enUS962US962&sxsrf=ALiCzsa2kbtP_BMPN3CT1bOnI-__sx6-Eg%3A1651122832916&ei=kCJqYuq8N8ib_QbclZCwDA&ved=0ahUKEwjqxL7v_7X3AhXITd8KHdwKBMYQ4dUDCA4&uact=5&oq=microsoft+stock+price+5+days&gs_lcp=Cgdnd3Mtd2l6EAMyBQghEKABMgUIIRCrAjoHCCMQsAMQJzoHCAAQRxCwAzoHCAAQsAMQQzoLCAAQgAQQsQMQgwE6BQgAEIAEOgYIABAWEB46BQgAEIYDOggIIRAWEB0QHkoECEEYAEoECEYYAFDxDVieJ2CIKmgBcAF4AIABeogB5gSSAQM2LjGYAQCgAQHIAQrAAQE&sclient=gws-wiz"
page = requests.get(URL)

formatted = page.text.split("<")

for index in formatted:
    if "BNeawe iBp4i AP7Wnd" in index:
        h=index.split(">")
        if h[-1] != "":
            price = print(h[-1].strip())
        

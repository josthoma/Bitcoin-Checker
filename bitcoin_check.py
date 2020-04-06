import requests
import urllib.request
import time
from bs4 import BeautifulSoup
from pprint import pprint as pp
import smtplib, ssl

port = 465  # For SSL
smtp_server = "smtp.gmail.com"
sender_email = ""  # Enter your address
receiver_email = ""  # Enter receiver address
receiver_email2 = ''
password = ''

while True:
    page = requests.get('https://markets.businessinsider.com/currencies/btc-usd').text

    #
    # url = 'https://api.coinmarketcap.com/v1/ticker/bitcoin/'
    # response = requests.get(url)
    # print(response)
    soup = BeautifulSoup(page, "lxml")
    # print(soup.prettify())
    # print(soup.findAll('a'))
    # print(soup)

    con = soup.find('span', {"class": "push-data"})
    content = (con.text).replace(',','')
    print(float(content))
    # pp(content.text)
    if (float(content) < 67):
        message = """\
        Subject: BUY :Bitcoin Price Change 
        
        Time to Buy.
        Current Price = """ +str(content)
        context = ssl.create_default_context()
        with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
            server.login(sender_email, password)
            server.sendmail(sender_email, receiver_email, message)
            server.sendmail(sender_email, receiver_email2, message)
    elif (float(content) > 9800):
        message = """\
        Subject: SELL :Bitcoin Price Change 

        Time to Sell.
        Current Price = """ + str(content)
        context = ssl.create_default_context()
        with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
            server.login(sender_email, password)
            server.sendmail(sender_email, receiver_email, message)
            server.sendmail(sender_email, receiver_email2, message)
    else:
        time.sleep(40)
        continue

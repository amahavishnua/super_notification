'''
from selenium import webdriver
p = "/Users/mvr/Downloads/chromedriver"
driver=webdriver.Chrome(p)

driver.get("https://newclasses.nyu.edu/portal/site/~mra503")
print(driver.title)
#driver.quit()
'''


import requests
url="https://www.google.com/search?q=NYSE:ORCL"
headerss={"User-Agent":'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36'}
import time
page=requests.get(url,headers=headerss)

from bs4 import BeautifulSoup
def target_alert(stock_name):
    
    url="https://www.google.com/search?q="+stock_name+"stock price"
    page=requests.get(url,headers=headerss)
    soup = BeautifulSoup(page.content,'html.parser')

    #print(soup.prettify())
    price = soup.findAll("span", {"jsname": "vWLAgc"})
    #for span in price:
        #if span.find_all('class'='cwUqwd'):
            #print(soup.find(class="cwUqwd"))

    print(price[0])

    print(price[0].get_text())

    price_of_stock=float(price[0].get_text())

    if (price_of_stock>63):
        send_notification(stock_name,price_of_stock)


import smtplib

def send_notification(stck_name,stck_price):
    server=smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.ehlo()
    server.login('mravishnu2@gmail.com','King@1998')
    subject="PROFITTT "+stck_name
    body=" its currently at "+str(stck_price)
    message=f"Subject:{subject}\n\n{body}"
    server.sendmail(
        'mravishn2@gmail.com',
        'mra503@nyu.edu',
        message
    )
    print("Profitsss MTFCKR")
    server.quit()

from datetime import datetime
from threading import Timer

x=datetime.today()
y=x.replace(day=x.day+1, hour=9, minute=0, second=0, microsecond=0)
delta_t=y-x
print(x)
print(y)
print(delta_t)
secs=delta_t.total_seconds()
print(secs)
t = Timer(secs, target_alert("oracle"))
t.start()
'''
while(True and ):
    target_alert("oracle")
    time.sleep(60)
    '''
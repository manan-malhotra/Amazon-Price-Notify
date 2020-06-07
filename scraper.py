import requests
from bs4 import BeautifulSoup
import smtplib
import time

url = "https://www.amazon.in/gp/product/B07J3CJM4N/ref=s9_acss_bw_cg_CPACS_5d1_w?pf_rd_m=A1K21FY43GMZF8&pf_rd_s=merchandised-search-8&pf_rd_r=DZJ3FCHGSBXRKYK9WBVQ&pf_rd_t=101&pf_rd_p=3b6413f1-424f-448e-b56c-409860ffe8c7&pf_rd_i=1389401031"

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36 Edg/83.0.478.45"
}


def check_price():
    page = requests.get(url, headers=headers)
    soup = BeautifulSoup(page.content, "html.parser")
    price = soup.find(id="priceblock_ourprice").get_text()
    converted_price = int((price[2:8]).replace(",", ""))
    if converted_price < 65000:
        send_mail()
    print(converted_price)


def send_mail():
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.ehlo()
    server.starttls()
    server.ehlo()

    server.login("manan221199@gmail.com", "tnkndkqhqhhdiewi")
    subject = "Price Down"
    body = "Check the amazon link: \n https://www.amazon.in/gp/product/B07J3CJM4N/ref=s9_acss_bw_cg_CPACS_5d1_w?pf_rd_m=A1K21FY43GMZF8&pf_rd_s=merchandised-search-8&pf_rd_r=DZJ3FCHGSBXRKYK9WBVQ&pf_rd_t=101&pf_rd_p=3b6413f1-424f-448e-b56c-409860ffe8c7&pf_rd_i=1389401031"

    msg = f"Subject:{subject}\n\n{body}"

    server.sendmail("manan221199@gmail.com", "manan221199@gmail.com", msg)

    server.quit()
    print("Mail sent!!")


i = 0
while i != 5:
    check_price()
    time.sleep(43200)
    i += 1

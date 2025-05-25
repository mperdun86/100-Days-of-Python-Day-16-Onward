import os

import requests
from bs4 import BeautifulSoup
import smtplib
from dotenv import load_dotenv

load_dotenv()

SMTP_ADDRESS = os.getenv("SMTP_ADDRESS")
EMAIL_ADDRESS = os.getenv("EMAIL_ADDRESS")
EMAIL_PASSWORD = os.getenv("EMAIL_PASSWORD")
URL = "https://www.amazon.com/CanaKit-Raspberry-Starter-Kit-PRO/dp/B0CRSNCJ6Y/ref=sr_1_1?crid=11NNEHHBKWA8X&dib=eyJ2IjoiMSJ9.vCrg1_s9-d710VGX_QZKTHLnjxLbsTSCxMN6MbXupywtWRRuuEv8l9HFn3LXXaDfipwgOFVA0HKHhZdV4gLEjsxW3cXam7YvwrHjxvdsv7kzyVIN9sWhd7fDQQmnZkOwFdnDps3nGoo2a6kHpE4gKBP_zvq6B9FROLELWuzBJWQQJ-eQuVGCMpMYoJiVSqT6ZThCTOs-xDPD2bJyfjXC25gEuHT1XOklrClf8velAwk.DcDiWDCWTomxdI_8IF0cTZf2s_e7sCbt4yaMnXehArU&dib_tag=se&keywords=raspberry%2Bpi&qid=1748194902&sprefix=raqspberry%2Caps%2C149&sr=8-1&th=1"
HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                  "AppleWebKit/537.36 (KHTML, like Gecko) "
                  "Chrome/120.0.0.0 Safari/537.36"
}

response = requests.get(URL, headers=HEADERS)
soup = BeautifulSoup(response.text, "html.parser")

apex_div = soup.find('div', id='apex_desktop')

price_whole = soup.find('div', id='apex_desktop').find('span', class_='a-price-whole').text.strip()
price_fraction = soup.find('div', id='apex_desktop').find('span', class_='a-price-fraction').text.strip()
total_price = float(price_whole + price_fraction)
print(total_price)

if total_price < 140:
    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=EMAIL_ADDRESS, password=EMAIL_PASSWORD)

        subject = "Price Alert: Raspberry PI Kit"
        body = f"Go check out {URL}, the price has dropped to ${total_price}!"
        msg = f"Subject: {subject}\n\n{body}"

        connection.sendmail(
            from_addr=EMAIL_ADDRESS,
            to_addrs=EMAIL_ADDRESS,
            msg=msg.encode("utf-8")
        )
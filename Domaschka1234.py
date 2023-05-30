import sqlite3

connection = sqlite3.connect("itstep_SB.sl3", 5)
cur = connection.cursor()

from bs4 import BeautifulSoup
import requests
respones = requests.get("https://sinoptik.ua/погода-берлин-102950159")





cur.execute("CREATE TABLE perscha_table (Date TEXT);")
connection.commit()
cur.execute("CREATE TABLE perscha_table (Time TEXT);")
connection.commit()
cur.execute("CREATE TABLE perscha_table (Temperature TEXT);")
connection.commit()

if respones.status_code == 200:
     soup = BeautifulSoup(respones.text, features="html.parser")
     soup_list = soup.find_all("p", class_="today-temp")
     res = soup_list[0].find("span")
     print(res)

if respones.status_code == 200:
     soup = BeautifulSoup(respones.text, features="html.parser")
     soup_list = soup.find_all("p", class_="today-time")
     res = soup_list[0].find("span")
     print(res)

if respones.status_code == 200:
     soup = BeautifulSoup(respones.text, features="html.parser")
     soup_list = soup.find_all("p", class_="date ")
     res = soup_list[0].find("span")
     print(res)
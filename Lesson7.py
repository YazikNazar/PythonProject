# # import urllib.request
# import requests
# res_parse_list = []
# #
# # opener = urllib.request.build_opener()
# # response = opener.open("https://httpbin.org/get")
# # print(response.read())
# #
# # response = requests.get("https://httpbin.org/get")
# # print(response.content)
# # # print(f"Datatype - {type(response.text)}")
#
# response = requests.get("https://coinmarketcap.com/")
# response_text = response.text
# response_parse = response_text.split("<span>")
# for parse_elem_1 in  response_parse:
#     if parse_elem_1.startswith("$"):
#        for parse_elem_2 in parse_elem_1.split("</span>"):
#            if parse_elem_2.startswith("$") and parse_elem_2[1].isdigit():
#                res_parse_list.append(parse_elem_2)
#
# bitcoin_exchange_rate = res_parse_list[0]
# print(bitcoin_exchange_rate)


from bs4 import BeautifulSoup
import requests
respones = requests.get("https://www.oschadbank.ua/currency-rate")

if respones.status_code == 200:
     soup = BeautifulSoup(respones.text, features="html.parser")
     soup_list = soup.find_all("div", class_="heading-block-currency-rate__table-txt body-regular")
     res = soup_list.find("td")
     print(res.text)


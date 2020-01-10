from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup

my_url="http://dict.cn/rule"

#opening up connection, grabbing the page
uClient = uReq(my_url)
page_html = uClient.read()
uClient.close()

page_soup = soup(page_html,"html.parser")
phonetic_symbols=page_soup.find_all("bdo")
print(phonetic_symbols[0],phonetic_symbols[1])
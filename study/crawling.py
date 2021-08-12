import requests
from bs4 import BeautifulSoup
webpage = requests.get("https://www.naver.com/")
soup = BeautifulSoup(webpage.content, "html.parser")

print(soup.find_all("div"))

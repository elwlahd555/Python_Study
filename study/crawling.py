import requests
from bs4 import BeautifulSoup
webpage = requests.get("https://shopping.naver.com/")
soup = BeautifulSoup(webpage.content, "html.parser")
text = soup.text
print(text)

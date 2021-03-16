import requests
from bs4 import BeautifulSoup
import re

url = input("Voer een URL in ")
request = requests.get(url).text
soup = BeautifulSoup(request, "html.parser")
text = soup.getText()

pattern = ".*@.*\\.nl"
email = re.findall(pattern, text)

for mail in email:
    print(mail)

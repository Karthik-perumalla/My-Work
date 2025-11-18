import requests
import pandas as pd

url = "https://en.wikipedia.org/wiki/The_World%27s_Billionaires"

h = {
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
    }
response = requests.get(url, headers=h)

tables = pd.read_html(response.text)

print(tables[0])
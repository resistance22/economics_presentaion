from bs4 import BeautifulSoup
import pandas as pd
import requests


def is_float(val):
    try:
        float(val)
        return True
    except:
        return False


df_values = {"Date": [], "employment_rate": []}

with open("./employment.html", "r") as f:
    html = f.read()
    soup = BeautifulSoup(html, features="html.parser")
    found_TBL = soup.find("table")
    for tr in found_TBL.find_all("tr")[1:]:
        tds = tr.find_all("td")
        year = 0
        for index, td in enumerate(tds):
            if index == 0:
                year = td.text
            if index != 0 and is_float(td.text):
                df_values["Date"].append(f"{year}-{'{:02d}'.format(index)}-01")
                df_values["employment_rate"].append(float(td.text))


print(df_values)

df = pd.DataFrame(df_values)
df.to_csv("./Data/employment.csv", index=False)

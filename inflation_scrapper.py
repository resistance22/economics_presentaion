from bs4 import BeautifulSoup
import pandas as pd
import requests

df_values = {"Date": [], "inflation_rate": []}

with open("./data.html", "r") as f:
    html = f.read()
    soup = BeautifulSoup(html, features="html.parser")
    found_TBL = soup.find("table")
    for tr in found_TBL.find_all("tr")[1:]:
        year = tr.find("th").text
        tds = tr.find_all("td")
        for index, td in enumerate(tds):
            if (
                index != 12
                and td.text != "\xa0"
                and "Avail" not in td.text
                # and int(year) >= 1947
                # and index in [0, 3, 6, 9]
            ):
                df_values["Date"].append(f"{year}-{'{:02d}'.format(index+1)}-01")
                df_values["inflatoin_rate"].append(float(td.text))
                # df_values[] = float(td.text)


df = pd.DataFrame(df_values)
df.to_csv("./Data/Inflation.csv", index=False)

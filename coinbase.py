import requests
import csv
import pandas as pd
import os


# Define API Endpoint
URL='http://api.coincap.io/v2/assets'


# Make Request
try:
    r=requests.get(URL)
    # print(r.status_code==requests.codes.ok, r.encoding)

    # Convert to JSON
    data=r.json()

except requests.exceptions.RequestException as e:
    print(f'Failed to retrieve data. HTTP Status code: {r.status_code}')



# ETL
coin_list=[]
for x in data['data']:
    refined_data= {'symbol': x['symbol'],
                   'name': x['name'],
                   'price_usd': x['priceUsd']}
    coin_list.append(refined_data)


# Save as CSV
FILENAME='refined_coins.csv'

df=pd.DataFrame(coin_list)
df.to_csv(FILENAME, index=True)

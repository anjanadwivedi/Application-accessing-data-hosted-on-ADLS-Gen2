import pandas as pd 

url ="https://adfaw17.blob.core.windows.net/landing/orders.csv"

response  = pd.read_csv(url)
pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows',None)

print(response.head(5))

import os, re, requests
from bs4 import BeautifulSoup
import pandas as pd
import numpy as np

count = 0
_sanitize = lambda t:list(map(lambda x:re.sub(r'\s{2,}', '\t', x.text.strip().encode('ascii', 'ignore').decode().replace('\n', '\t')) ,t))

def _get_table_values(table):
    head = _sanitize(table.find_all('th'))
    data = _sanitize(table.find_all('td'))
    return (head,data)

def _get_dataframe(head, data, maxcount):
    global count
    count += 1
    try:
        d = np.array(data).reshape(int(len(data)/len(head)),len(head))
        df = pd.DataFrame(d)
        df.columns = head
    except:
        print(f"Skipping table ({count}/{maxcount}) for re-shaping error")
        df = pd.DataFrame()
        pass
    return df

def _convert_tables_to_dataframes(url):
    res = requests.get(f"{url}", headers={'user-agent':'IAMAI'})
    html = BeautifulSoup(res.content, features='lxml')
    tables = html.select('table')
    return list(map(lambda r:_get_dataframe(r[0],r[1],len(tables)), map(_get_table_values, tables)))

def get_stock_prediction(stock='NVDA', url='https://coincodex.com/stock/'):
    dfs = _convert_tables_to_dataframes(f"{url}/{stock}/price-prediction/")
    class result:
        current = dfs[0]
        long_term = dfs[1]
        sma_day = dfs[2]
        ema_day = dfs[3]
        sma_week = dfs[4]
        ema_week = dfs[5]
        week_forecast = dfs[6]
        yoy_history = dfs[8]
    return result

def get_crypto_prediction(crypto='bitcoin', url='https://coincodex.com/crypto/'):
    dfs = _convert_tables_to_dataframes(f"{url}/{crypto}/price-prediction/")
    class result:
        current = dfs[0]
        long_term = dfs[1]
        sma_day = dfs[2]
        ema_day = dfs[3]
        sma_week = dfs[4]
        ema_week = dfs[5]
        oscillators = dfs[6]
        support = dfs[7]
        resistance = dfs[8]
        positive_rho = dfs[9]
        negative_rho = dfs[10]
        week_forecast = dfs[11]
        yoy_history = dfs[13]
    return result
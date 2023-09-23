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

def get_congress_trading(url='https://www.quiverquant.com/congresstrading/'):
    dfs = _convert_tables_to_dataframes(url)
    class result:
        recent_trades = dfs[0]
        active_traders = dfs[1]
    return result

def get_senate_trading(url='https://www.quiverquant.com/sources/senatetrading'):
    dfs = _convert_tables_to_dataframes(url)
    class result:
        recent_trades = dfs[0]
    return result

def get_house_trading(url='https://www.quiverquant.com/sources/housetrading'):
    dfs = _convert_tables_to_dataframes(url)
    class result:
        recent_trades = dfs[0]
        recent_trades_options = dfs[1]
    return result

def get_election_contributions(url='https://www.quiverquant.com/election-contributions/'):
    dfs = _convert_tables_to_dataframes(url)
    class result:
        pac_donations = dfs[0]
        employee_donations = dfs[1]
    return result

def get_dc_insider_scores(url='https://www.quiverquant.com/scores/dcinsider'):
    dfs = _convert_tables_to_dataframes(url)
    class result:
        top_insiders = dfs[0]
    return result

def get_gov_contracts(url='https://www.quiverquant.com/sources/govcontracts'):
    dfs = _convert_tables_to_dataframes(url)
    class result:
        recent_contracts = dfs[0]
    return result

def get_lobbying(url='https://www.quiverquant.com/lobbying/'):
    dfs = _convert_tables_to_dataframes(url)
    class result:
        recent_disclosures = dfs[0]
        top_spenders = dfs[1]
    return result

def get_inflation(url='https://www.quiverquant.com/inflation/'):
    dfs = _convert_tables_to_dataframes(url)
    class result:
        inflation_risk_score = dfs[0]
    return result

def get_insiders(url='https://www.quiverquant.com/insiders/'):
    dfs = _convert_tables_to_dataframes(url)
    class result:
        recent_activity = dfs[0]
    return result

def get_insider_tracker(url='https://www.quiverquant.com/insidertracker/'):
    dfs = _convert_tables_to_dataframes(url)
    class result:
        notable_insiders = dfs[0]
    return result

def get_stock_splits(url='https://www.quiverquant.com/stocksplits/'):
    dfs = _convert_tables_to_dataframes(url)
    class result:
        recent_8k_filings = dfs[0]
    return result
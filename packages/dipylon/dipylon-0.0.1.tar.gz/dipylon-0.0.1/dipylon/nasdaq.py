import os, json, requests
from requests.models import PreparedRequest
import pandas as pd

def get_insider_trades(ticker, url='https://api.nasdaq.com', limit=15, offset=0, queryType='ALL', sortColumn='lastDate', softOrder='DESC'):
	"""
	:params ticker: `str` of ticker symbol to query (ex: nvda, pstg)
	:return: `pandas.DataFrame` object of returned data from API response
	"""
	req = PreparedRequest()
	req.prepare_url(f"{url}/api/company/{ticker}/insider-trades", {'limit':limit, 'offset':offset, 'type':queryType, 'sortColumn':sortColumn, 'sortOrder':softOrder})
	res = requests.get(req.url, headers={'referer':'https://api.nasdaq.com/', 'user-agent':'Mozilla/X.X (IAMAI) AppleWebKit/X.X (IAMAI) Chrome/128.0.0.0 Safari/X.X'})
	if not res.ok:
		print('API response is invalid')
		os._exit(1)
	ret = json.loads(res.content)
	if ret['status']['rCode'] != 200:
		print('API response error occurred')
		os._exit(2)
	return pd.DataFrame(ret['data']['transactionTable']['table']['rows']).drop('url', axis=1)
import os, json, requests
from requests.models import PreparedRequest
import pandas as pd

_sanitize_ticker = lambda rt:rt.strip('$').upper()

def get_timeseries(ticker, url='https://query1.finance.yahoo.com', region='US', interval='2m', range='1d'):
	"""
	:params ticker: `str` of ticker symbol (ex: NVDA, BTC-USD)
	:return: `pandas.DataFrame`
	"""
	params = {'lang':'en-US', 'includePrePost':'false', 'useYfid':'true', 'corsDomain':'finance.yahoo.com', '.tsrc':'finance'}
	params.update({'region':region, 'interval':interval, 'range':range})
	req = PreparedRequest()
	req.prepare_url(f"{url}/v8/finance/chart/{_sanitize_ticker(ticker)}", params)
	res = requests.get(req.url, headers={'User-Agent': 'IAMAI', 'From': 'i@m.ai'})
	if res.ok:
		data = json.loads(res.content)
	else:
		print(f"Data unobtainable from API")
		os._exit(1)
	return pd.DataFrame(data['chart']['result'][0]['indicators']['quote'][0], index=pd.to_datetime(data['chart']['result'][0]['timestamp'], unit='s'))

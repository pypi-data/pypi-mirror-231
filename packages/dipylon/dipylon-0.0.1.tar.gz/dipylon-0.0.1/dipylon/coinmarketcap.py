import os, json, requests
from requests.models import PreparedRequest

def get_market_pairs(slug='bitcoin', url='https://api.coinmarketcap.com', start=1, limit=10):
	"""
	:params slug: `str` of ticker slug (ex: bitcoin, dogecoin)
	:return: `tuple` of slug as ticker `str` and weighted price as `float`
	"""
	params = {'category':'spot', 'centerType':'all', 'sort':'cmc_rank_advanced', 'direction':'desc'}
	params.update({'slug':slug, 'start':start, 'limit': limit})
	req = PreparedRequest()
	req.prepare_url(f"{url}/data-api/v3/cryptocurrency/market-pairs/latest", params)
	res = requests.get(req.url, headers={'User-Agent': 'IAMAI', 'From': 'i@m.ai'})
	if res.ok:
		data = json.loads(res.content)
	if int(data['status']['error_code']) == 500:
		print(f"Error: the slug value `args.slug` was not found")
		os._exit(1)
	mpv = list(map(lambda x:(x['marketPair'],x['price'],x['volumePercent']), data['data']['marketPairs']))
	v = [vp[2] for vp in mpv]
	x = [vp[1]*vp[2]/sum(v) for vp in mpv]
	class result:
		symbol = data['data']['symbol']
		prices = x
	return result
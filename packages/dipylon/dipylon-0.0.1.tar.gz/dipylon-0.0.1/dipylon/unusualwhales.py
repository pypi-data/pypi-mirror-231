import os, json, requests
from datetime import datetime, timedelta
from requests.models import PreparedRequest
import pandas as pd
import numpy as np

class defaults:
    date = datetime.now().strftime('%Y-%m-%d')
    end_date = (datetime.now()+timedelta(days=7)).strftime('%Y%m%d')

def get_data_from_api(url, params={}):
    req = PreparedRequest()
    req.prepare_url(f"{url}", params)
    res = requests.get(req.url, headers={'User-Agent': 'IAMAI'})
    if res.ok:
        data = json.loads(res.content)
    else:
        print(f"Data unavailable from API")
        os._exit(1)
    return data

def get_option_trades(url='https://phx.unusualwhales.com/api/option_trades/free', limit=50):
    return pd.DataFrame(get_data_from_api(url, {'limit': limit})['data'])

def get_hot_chains(url='https://phx.unusualwhales.com/api/hot_chains', limit=100):
    return pd.DataFrame(get_data_from_api(url, {'limit': limit})['data'])

def get_flow_expiry_dates(url='https://phx.unusualwhales.com/api/flow/util/expiry_dates', symbol='undefined', version='v2'):
    return pd.DataFrame(get_data_from_api(f"{url}_{version}", {'symbol': symbol})['data'])

def get_flow_alerts(url='https://phx.unusualwhales.com/api/flow/alerts', limit=50):
    return pd.DataFrame(get_data_from_api(url, {'limit': limit})['alerts'])

def get_oi_chains(url='https://phx.unusualwhales.com/api/oi_changes/chains', limit=50):
    return pd.DataFrame(get_data_from_api(url, {'limit': limit})['data'])

def get_option_delivery(url='https://phx.unusualwhales.com/api/option/delivery'):
    return pd.DataFrame(get_data_from_api(url)['data'])

def get_net_flow(url='https://phx.unusualwhales.com/api/net_flow', date=defaults.date):
    return pd.DataFrame(get_data_from_api(url, {'date': date})['data'])

def get_one_minute_ticker_candles(company, url='https://phx.unusualwhales.com/api/ticker_candles', date=defaults.date):
    return pd.DataFrame(get_data_from_api(f"{url}/{company}/one_minute", {'date': date})['data'])

def get_news_headlines(url='https://phx.unusualwhales.com/api/news/headlines-feed', limit=100):
    return pd.DataFrame(get_data_from_api(url, {'limit': limit})['data'])

def get_earnings_calendar(url='https://phx.unusualwhales.com/api/earnings/calendar', formats='calendar', min_date=defaults.date, max_date=defaults.end_date):
    return pd.DataFrame(get_data_from_api(url, {'formats': formats, 'min_date': min_date, 'max_date': max_date})['data'])

def get_upcoming_splits(url='https://phx.unusualwhales.com/api/splits/upcoming'):
    return pd.DataFrame(get_data_from_api(url)['data'])

def get_upcoming_dividends(url='https://phx.unusualwhales.com/api/dividends/upcoming', limit=50):
    return pd.DataFrame(get_data_from_api(url, {'limit': limit})['data'])

def get_trading_states(url='https://phx.unusualwhales.com/api/trading_states'):
    return pd.DataFrame(get_data_from_api(url))

def get_insider_trades_monthly(url='https://phx.unusualwhales.com/api/insider_trades_monthly', limit=50, order='buy_perc', order_direction='desc'):
    return pd.DataFrame(get_data_from_api(url, {'limit': limit, 'order': order, 'order_direction': order_direction})['data'])

def get_volatility_index(url='https://phx.unusualwhales.com/api/volatility_index', date=defaults.date, lookback=90):
    return pd.DataFrame(get_data_from_api(url, {'date': date, 'lookback': lookback})['data'])

def get_historical_prices(company, url='https://phx.unusualwhales.com/api/companies', limit=2):
    return pd.DataFrame(get_data_from_api(f"{url}/{company}/get_historical_prices", {'limit': limit})['history'])

def get_tradex_news(company, url='https://phx.unusualwhales.com/api/tradex_news', offset=0, limit=50):
    params = {'tickers': company, 'ticker': company, 'search_term': company, 'offset': offset, 'limit': limit}
    return pd.DataFrame(get_data_from_api(url, params)['data'])

def get_intraday(company, url='https://phx.unusualwhales.com/api/ticker_aggregates', date=defaults.date, grouping_minutes=5, market_day_timeframe=1):
    params = {'date': date, 'grouping_minutes': grouping_minutes, 'market_day_timeframe': market_day_timeframe}
    res = get_data_from_api(f"{url}/{company}/intraday", params)
    return pd.merge(pd.DataFrame(res['data']), pd.DataFrame(res['underlying_data']), left_on='tape_time', right_on='start_time')

def get_gex(company, url='https://phx.unusualwhales.com/api/gex', date=defaults.date, timespan='1y'):
    return pd.DataFrame(get_data_from_api(f"{url}/{company}", {'timespan': timespan, 'date': date})['data'])

def get_top_chains_by_open_interest(company, url='https://phx.unusualwhales.com/api/top_chains_by_open_interest', date=defaults.date):
    return pd.DataFrame(get_data_from_api(f"{url}/{company}", {'date': date})['chains'])

def get_top_chains_by_volume(company, url='https://phx.unusualwhales.com/api/top_chains_by_volume', date=defaults.date):
    return pd.DataFrame(get_data_from_api(f"{url}/{company}", {'date': date})['chains'])

def get_company(company, url='https://phx.unusualwhales.com/api/companies'):
    return pd.DataFrame(get_data_from_api(f"{url}/{company}", {'thin': 'true'}))

def get_crypto_options(url='https://phx.unusualwhales.com/api/crypto_options'):
    return pd.DataFrame(get_data_from_api(url))

def get_crypto_whales(url='https://phx.unusualwhales.com/api/crypto_whales'):
    return pd.DataFrame(get_data_from_api(url))

def get_option_all():
    class result:
        net_flow = get_net_flow()
        flow_expiry_dates = get_flow_expiry_dates()
        flow_alert = get_flow_alerts()
        oi_chains = get_oi_chains()
        option_trades = get_option_trades()
        option_delivery = get_option_delivery()
        hot_chains = get_hot_chains()
    return result

def get_market_all():
    class result:
        news_headlines = get_news_headlines()
        earnings_calendar = get_earnings_calendar()
        upcoming_splits = get_upcoming_splits()
        upcoming_dividends = get_upcoming_dividends()
        trading_states = get_trading_states()
        insider_trades_monthly = get_insider_trades_monthly()
        volatility_index = get_volatility_index()
    return result

def get_crypto_all():
    class result:
        crypto_options = get_crypto_options()
        crypto_whales = get_crypto_whales()
    return result

def get_company_all(company):
    com = company
    class result:
        summary = get_company(com)
        gex = get_gex(com)
        intraday = get_intraday(com)
        tradex_news = get_tradex_news(com)
        one_minute_ticker_candles = get_one_minute_ticker_candles(com)
        historical_prices = get_historical_prices(com)
        top_chains_by_open_interest = get_top_chains_by_open_interest(com)
        top_chains_by_volume = get_top_chains_by_volume(com)
    return result
def simplify_data(data):
    simplified_data = []
    time_series = data.get('Time Series (5min)', {})
    query = data.get('Meta Data', {})
    symbol = query.get('2. Symbol', 'N/A')
    last_refreshed = query.get('3. Last Refreshed', 'N/A')
    query = {
        'symbol': symbol,
        'last_refreshed': last_refreshed
    }
    simplified_data.append(query)

    for i, (key, value) in enumerate(time_series.items()):
        if i >= 5:
            break
        simplified_data.append({
            'time': key,
            'open': value.get('1. open', 'N/A'),
            'high': value.get('2. high', 'N/A'),
            'low': value.get('3. low', 'N/A'),
            'close': value.get('4. close', 'N/A'),
            'volume': value.get('5. volume', 'N/A')
        })
    
    return simplified_data
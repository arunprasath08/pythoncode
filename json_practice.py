json={
   "time": {      "updated": "Jun 7, 2022 18:54:00 UTC",      "updatedISO": "2022-06-07T18:54:00+00:00",      "updateduk": "Jun 7, 2022 at 19:54 BST"   },
   "disclaimer": "This data was produced from the CoinDesk Bitcoin Price Index (USD). Non-USD currency data converted using hourly conversion rate from openexchangerates.org",
   "chartName": "Bitcoin",
   "bpi": {
      "USD": { "code": "USD", "symbol": "&#36;", "rate": "30,161.3251", "description": "United States Dollar", "rate_float": 30161.3251 },
      "GBP": { "code": "GBP", "symbol": "&pound;", "rate": "24,115.2462", "description": "British Pound Sterling","rate_float": 24115.2462 },
      "EUR": { "code": "EUR", "symbol": "&euro;", "rate": "28,236.4595", "description": "Euro","rate_float": 28236.4595 }
   }
}

##'''Access first level nodes'''
##
##for node in json:
##    print(node,':',json[node])
##
##'''Access second level nodes'''
##
##for node in json['time']:
##    print(node,':',json['time'][node])
##
##'''Access third level nodes'''
##
##for node in json['bpi']['USD']:
##    if node=='rate':
##        print(node,':',json['bpi']['USD'][node])

for lev1_node in json:
    for lev2_node in json[lev1_node]:
        print(lev2_node)
        #for lev3_node in json[lev2_node]:
            

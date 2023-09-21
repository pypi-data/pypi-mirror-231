# Trading 212 API ( Beta )

This is a python wrapper for the trading 212 beta API. https://t212public-api-docs.redoc.ly/

## DISCLAIMER
The api is a straight mapping to the trading 212 endpoints.  
- No liability is assumed by me for you using this library.  
- Any trading activity you undertake using this library is solely your own responsibility. 
- No liability will be assumed if you lose your KEY.

## Installation
```
$ pip install trading-212
```

## Creating a client

You will need to create a API key from your trading 212 account. Follow trading212's instructions around usage and safeguarding this KEY.

```
>>> from trading212 import Client
>>> client = Client("YOUR_API_KEY")
```

## API

### Metadata

#### get_exchanges()

#### get_instruments()

### Pies

#### get_pies()

#### get_pie(id)
```id``` int, id of pie

#### create_pie(dividend_cash_action, end_date, goal, icon, instrument_shares, name)
```dividend_cash_action``` string, Enum: "REINVEST" "TO_ACCOUNT_CASH"

```end_date``` string, <date-time> isoformat

```goal``` int

```icon``` string, Enum: "Home" "PiggyBank" "Iceberg" "Airplane" "RV" "Unicorn" "Whale" "Convertable" "Family" "Coins" "Education" "BillsAndCoins" "Bills" "Water" "Wind" "Car" "Briefcase" "Medical" "Landscape" "Child" "Vault" "Travel" "Cabin" "Apartments" "Burger" "Bus" "Energy" "Factory" "Global" "Leaf" "Materials" "Pill" "Ring" "Shipping" "Storefront" "Tech" "Umbrella"

```instrument_shares``` dict, {ticker_name: float, quantity}

```name``` string,  name for pie

```
>>> client.create_pie("REINVEST", "2019-08-24T14:15:22Z", 0, "Home", {"AAPL_US_EQ": 0.5, "MSFT_US_EQ": 0.5}, "my pie")
```

#### update_pie(id, dividend_cash_action, end_date, goal, icon, instrument_shares, name)
```id``` int, id of pie

```dividend_cash_action``` string, Enum: "REINVEST" "TO_ACCOUNT_CASH"

```end_date``` string, <date-time> isoformat

```goal``` int

```icon``` string, Enum: "Home" "PiggyBank" "Iceberg" "Airplane" "RV" "Unicorn" "Whale" "Convertable" "Family" "Coins" "Education" "BillsAndCoins" "Bills" "Water" "Wind" "Car" "Briefcase" "Medical" "Landscape" "Child" "Vault" "Travel" "Cabin" "Apartments" "Burger" "Bus" "Energy" "Factory" "Global" "Leaf" "Materials" "Pill" "Ring" "Shipping" "Storefront" "Tech" "Umbrella"

```instrument_shares``` dict, {ticker_name: float, quantity}

```name``` string,  name for pie

```
>>> client.update_pie(1701, "REINVEST", "2019-08-24T14:15:22Z", 0, "Home", {"AAPL_US_EQ": 0.5, "MSFT_US_EQ": 0.5}, "my pie")
```

#### delete_pie(id)
```id``` int, id of pie

### Orders

#### get_orders()

#### get_order(id)
```id``` int, id of order

#### delete_order(id)
```id``` int, id of order


#### place_limit_order(limit_price, quantity, ticker, time_validity)
```limit_price``` float

```quantity``` float

```ticker``` string	

```timeValidity``` string,  Enum: "DAY" "GTC"

```
>>> client.place_limit_order(122.31, .5, 'AAPL_US_EQ', 'GTC')
```

#### place_market_order(quantity, ticker)
```quantity``` float

```ticker``` string

```
>>> client.place_market_order(.5, 'AAPL')
```


#### place_stop_order(stop_price, quantity, ticker, time_validity)
```stop_price``` float

```quantity``` float

```ticker``` string	

```timeValidity``` string,  Enum: "DAY" "GTC"

```
>>> client.place_stop_order(122.31, .5, 'AAPL_US_EQ', 'GTC')
```


#### place_stop_limit_order(limit_price, stop_price, quantity, ticker, time_validity)
```limit_price``` float

```stop_price``` float

```quantity``` float

```ticker``` string	

```timeValidity``` string,  Enum: "DAY" "GTC"

```
>>> client.place_stop_order(122.31, 122.31, .5, 'AAPL_US_EQ', 'GTC')
```

### Account

#### get_account_cash()

#### get_account()

### Positions

#### get_positions()

#### get_position(id)
```id``` int, id of position

### Historical items

#### get_order_history(cursor, ticker, limit)
```cursor``` int <int64> Pagination cursor

```ticker``` string

```limit```	int <int32> Default: 20

```
>>> client.get_order_history(1, 'AAPL_EQ_US', 25)
```

#### get_dividends(cursor, ticker, limit)
```cursor``` int <int64> Pagination cursor

```ticker``` string

```limit```	int <int32> Default: 20

```
>>> client.get_dividends(1, 'AAPL_EQ_US', 25)
```

#### get_exports()

#### get_transactions(cursor, limit)
```cursor``` int <int64> Pagination cursor

```limit```	int <int32> Default: 20

```
>>> client.get_transactions(1, 25)
```

#### get_export(data_included, time_from, time_to)
```data_included``` dict, {"includeDividends": True, "includeInterest": True, "includeOrders": True, "includeTransactions": True}

```time_from``` string, isoformat

```time_to``` string, isoformat
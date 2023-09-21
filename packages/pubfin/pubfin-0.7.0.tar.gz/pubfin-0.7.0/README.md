<!-- markdownlint-disable -->



# `pubfin`

## `This package provides a Findata class with built-in methods to query, save, and output (to Pandas DataFrame) reported financial data via the SEC EDGAR API.`

## <kbd>class</kbd> `Findata`






### <kbd>function</kbd> `__init__`

```python
__init__(
    cik: str,
    ticker: str = None,
    listing_country: str = 'USA',
    request_header: dict = {'User-Agent': 'Default default@msn.com'}
)
```








---



### <kbd>static method</kbd> `pubfin.load_from_ticker`

```python
load_from_ticker(
    ticker: str,
    listing_country: str = 'USA',
    request_header: dict = {'User-Agent': 'Default default@msn.com'}
)
```

Constructs a Findata object using the supplied ticker symbol, looks up the matching SEC CIK id, and queries all available company fact data from the EDGAR API. Currently, this will only work for USA-listed companies accessible through the SEC EDGAR system. This function uses two SEC EDGAR API calls--one to look up the company's CIK id from ticker, and another to load reported financial data. 



**Args:**
 
 - <b>`ticker (str) `</b>:  The company's stock ticker symbol 
 - <b>`listing_country (str, optional) `</b>:  The company's listing country. Defaults to "USA" 
 - <b>`request_header (dict, optional) `</b>:  Your name and email, which is required by the SEC's APIs. Defaults to ``{ "User-Agent": "Default default@msn.com", }`` 



**Returns:**
 
 - <b>`Findata`</b>:  A Findata object with populated reported financial data (``self.data`` attribute) in a dict representation of the EDGAR API's JSON output. 

---



### <kbd>instance method</kbd> `pubfin.Findata.to_df`

```python
Findata.to_df(xbrl_tags: list = None)
```

Outputs a ``Findata`` object's dict representation of reported financial data to a flat Pandas dataframe. 



**Args:**
 
 - <b>`xbrl_tags`</b> (list, optional):  List of xbrl tag names (string format) to limit the output dataframe. Defaults to None. 



**Returns:**
 Pandas dataframe 




---

_This file was automatically generated via [lazydocs](https://github.com/ml-tooling/lazydocs)._

import pandas as pd
import upath as up
import datetime as dt
from urllib.request import Request, urlopen
import json


class Findata:
    sec_cik_json_path = up.UPath("https://www.sec.gov/files/company_tickers.json")

    def __init__(
        self,
        cik: str,
        ticker: str = None,
        listing_country: str = "USA",
        request_header: dict = {
            "User-Agent": "Default default@msn.com",
        },
    ):
        self.ticker = ticker
        self.listing_country = listing_country
        self.CIK = cik
        self.request_header = request_header

        # Data loading attributes
        self.data = None
        self.dataloadstatus = (False, dt.datetime(year=1900, month=1, day=1))

    @classmethod
    def __from_ticker(
        cls,
        ticker: str,
        listing_country: str = "USA",
        request_header: dict = {
            "User-Agent": "Default default@msn.com",
        },
    ):
        """
        Constructs a Findata object using the supplied ticker symbol and looks up the matching SEC CIK id.
        Currently, this will only work for USA-listed companies accessible through the SEC EDGAR system.

        Args:
            ticker (str) : The company's stock ticker symbol
            listing_country (str, optional) : The company's listing country. Defaults to "USA"
            request_header (dict, optional) : Your name and email, which is required by the SEC's APIs. Defaults to ``{ "User-Agent": "Default default@msn.com", }``

        Returns:
            Findata: A Findata object
        """
        json_req = Request(cls.sec_cik_json_path.path, headers=request_header)
        raw_dict = json.load(urlopen(json_req, timeout=10))
        if "1" in raw_dict.keys():
            raw_sec_cik_df = pd.DataFrame(
                [raw_dict[x] for x in raw_dict.keys()], dtype="str"
            )
            raw_sec_cik_df = raw_sec_cik_df.drop_duplicates(subset="ticker")
            raw_sec_cik_df = raw_sec_cik_df.set_index("ticker")
            clean_dict = raw_sec_cik_df.to_dict(orient="index")
            cik_lookup = clean_dict[ticker]["cik_str"]

            # Currently, SEC api query requires 10 digit CIK (starting zeroes)
            if len(cik_lookup) < 10:
                cik_lookup = "{:0>10}".format(cik_lookup)
        return cls(
            cik=cik_lookup,
            listing_country=listing_country,
            request_header=request_header,
            ticker=ticker,
        )

    @staticmethod
    def load_from_ticker(
        ticker: str,
        listing_country: str = "USA",
        request_header: dict = {
            "User-Agent": "Default default@msn.com",
        },
    ):
        """
        Creates a Findata object using the supplied ticker symbol, looks up the matching SEC CIK id, and queries all available company fact data from the EDGAR API.
        Currently, this will only work for USA-listed companies accessible through the SEC EDGAR system.
        This function uses two SEC EDGAR API calls--one to look up the company's CIK id from ticker, and another to load reported financial data.

        Args:
            ticker (str) : The company's stock ticker symbol
            listing_country (str, optional) : The company's listing country. Defaults to "USA"
            request_header (dict, optional) : Your name and email, which is required by the SEC's APIs. Defaults to ``{ "User-Agent": "Default default@msn.com", }``

        Returns:
            Findata: A Findata object with populated reported financial data (``self.data`` attribute) in a dict representation of the EDGAR API's JSON output.
        """
        loaded_findata_object = Findata.__from_ticker(
            ticker=ticker,
            listing_country=listing_country,
            request_header=request_header,
        )
        loaded_findata_object.__load_data()
        return loaded_findata_object

    def __load_data(self):
        """Queries SEC EDGAR API for all reported financial data."""
        try:
            # One api call which returns all company data
            drct_path = up.UPath(
                f"https://data.sec.gov/api/xbrl/companyfacts/CIK{self.CIK}.json"
            )
            req = Request(
                drct_path.path,
                headers=self.request_header,
            )
            sec_query_loaded = urlopen(req, timeout=10)
            raw_json = json.load(sec_query_loaded)

            self.dataloadstatus = (True, dt.datetime.now())
            self.data = raw_json
        except:
            self.dataloadstatus = (False, dt.datetime.now())

        return

    def to_df(self, xbrl_tags: list = None):
        """Outputs a ``Findata`` object's dict representation of reported financial data to a flat Pandas dataframe.

        Args:
            xbrl_tags (list, optional): List of xbrl tag names (string format) to limit the output dataframe. Defaults to None.

        Returns:
            Pandas dataframe
        """
        out_df = pd.DataFrame()

        for taxonomy in list(self.data["facts"].keys()):
            raw_df = pd.DataFrame(self.data["facts"][taxonomy])
            tags_list = raw_df.columns.to_list()

            for attribute in tags_list:
                attribute_keys = list(raw_df[attribute]["units"].keys())
                for key in attribute_keys:
                    curr_df = pd.DataFrame(raw_df[attribute]["units"][key])
                    curr_df["tag"] = attribute
                    curr_df["label"] = raw_df[attribute]["label"]
                    curr_df["description"] = raw_df[attribute]["description"]
                    curr_df["units"] = key
                    curr_df["taxonomy"] = taxonomy
                    out_df = pd.concat([out_df, curr_df], ignore_index=True)

        try:
            out_df = out_df.reindex(
                columns=[
                    "start",
                    "end",
                    "fy",
                    "fp",
                    "tag",
                    "label",
                    "description",
                    "val",
                    "units",
                    "form",
                    "filed",
                    "frame",
                    "accn",
                    "taxonomy",
                ]
            )
        except:
            pass

        if xbrl_tags:
            out_df = out_df.query("tag==@xbrl_tags")

        return out_df

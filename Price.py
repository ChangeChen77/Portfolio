# -*- coding: utf-8 -*-
"""
Created on Tue Nov 30 21:28:31 2021

@author: Change
"""

import yfinance as yf
import pandas as pd
import numpy as np


class GetInfoFromYM:
    def __init__(self, ticker, start_date, end_date):
        self.Ticker = ticker
        self.StartDate = start_date
        self.EndDate = end_date

        self.Result = {
            'AdjustedClosedPrice': ''
        }

    def get_adjusted_close_price(self):
        df = yf.download(self.Ticker, start=self.StartDate, end=self.EndDate)
        adj_closed_price = df['Adj Close']
        self.Result['AdjustedClosedPrice'] = adj_closed_price

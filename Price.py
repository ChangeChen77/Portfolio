# -*- coding: utf-8 -*-
"""
Created on Tue Nov 30 21:28:31 2021

@author: Change
"""

import yfinance as yf
import pandas as pd
import numpy as np

class GetInfoFromYM:
    def __init__(self,Ticker,StartDate,EndDate):
        self.Ticker=Ticker
        self.StartDate=StartDate
        self.EndDate=EndDate
        
        self.Result={
            'AdjedClosedPrice':''
            }
    def GetAdjedClosePrice(self):
        df=yf.download(self.Ticker,start=self.StartDate,end=self.EndDate)
        AdjClosedPrice=df['Adj Close']
        self.Result['AdjedClosedPrice']=AdjClosedPrice

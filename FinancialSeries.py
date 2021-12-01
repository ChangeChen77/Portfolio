# -*- coding: utf-8 -*-
"""
Created on Wed Dec  1 22:22:19 2021

@author: Change
"""
import yfinance as yf
import pandas as pd
import numpy as np
import Price
class FinancialSeries:
    def __init__(self,AdjedClosedPrice_df):
        self.AdjedClosedPrice_df=AdjedClosedPrice_df
    def TransToDailyLnRet(self):
        df=self.AdjedClosedPrice_df.copy()
        df=np.log(df).diff(1)
        df.dropna(inplace=True)
        self.DailyLnRet=df
    def TransToCumLnRet(self):
        df=self.DailyLnRet.copy()
        df=np.exp(df.cumsum())-1
        self.DailyCumRet=df
    #def TransToDrawDown(slef):
        
def main():
    df=Price.GetInfoFromYM('VTI BND BLV TLT','2020-03-01','2021-1-31')
    df.GetAdjedClosePrice()
    AssetPool=FinancialSeries(df.Result['AdjedClosedPrice'])
    AssetPool.TransToDailyLnRet()
    AssetPool.TransToCumLnRet()
    AssetPool.DailyCumRet.plot.line()
main()
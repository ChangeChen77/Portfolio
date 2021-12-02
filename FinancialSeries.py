# -*- coding: utf-8 -*-
"""
Created on Wed Dec  1 22:22:19 2021

@author: Change
"""
import yfinance as yf
import pandas as pd
import numpy as np
import Price
import datetime
class FinancialSeries:
    def __init__(self,AdjedClosedPrice_df):
        self.AdjedClosedPrice_df=AdjedClosedPrice_df
    def TransToDailyLnRet(self):
        #將價格轉換為DailyLnRet
        df=self.AdjedClosedPrice_df.copy()
        df=np.log(df).diff(1)
        df.dropna(inplace=True)
        self.DailyLnRet=df
    def CalToCumLnRet(self):
        #計算累積報酬率，可搭配lineChart
        df=self.DailyLnRet.copy()
        df=np.exp(df.cumsum())-1
        self.DailyCumRet=df
    def CalEachYearRet(self):
        #計算每年的報酬率，可搭配BarChart
        df=self.DailyLnRet.copy()
        df['Year']=pd.DatetimeIndex(df.index).year
        dfGroupByYear=np.exp(df.groupby('Year').sum())-1
        self.EachYearRet=dfGroupByYear
    def RollingRet(self,m):
        #計算滾動報酬率，以月資料頻率，並且將報酬率轉為年化，可搭配LineChart
        df=self.DailyLnRet.copy()
        df['Year']=pd.DatetimeIndex(df.index).year
        df['Month']=pd.DatetimeIndex(df.index).month
        dfGroupByYM=df.groupby(['Year','Month']).sum()
        dfRollingYearlyRet=np.exp(dfGroupByYM.rolling(m).sum()*12/m)-1
        dfRollingYearlyRet.dropna(inplace=True)
        self.RollingYearlyRet=dfRollingYearlyRet
    #def TransToDrawDown(slef):
def main():
    df=Price.GetInfoFromYM('VNQ AOA SPY','2010-01-01','2021-12-31')
    df.GetAdjedClosePrice()
    AssetPool=FinancialSeries(df.Result['AdjedClosedPrice'])
    AssetPool.TransToDailyLnRet()
    AssetPool.CalToCumLnRet()
    AssetPool.CalEachYearRet()
    #AssetPool.EachYearRet.plot.bar()
    AssetPool.RollingRet(72)
    AssetPool.RollingYearlyRet.plot.line()
main()
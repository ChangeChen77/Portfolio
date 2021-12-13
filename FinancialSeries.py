# -*- coding: utf-8 -*-
"""
Created on Wed Dec  1 22:22:19 2021

@author: Change
"""
import pandas as pd
import numpy as np
import Price
import matplotlib.pyplot as plt


class FinancialSeries:
    def __init__(self, adjusted_closed_price_df):
        self.adjusted_closed_price_df = adjusted_closed_price_df
        # 回傳值
        self.DailyLnRet = ''
        self.DailyCumRet = ''
        self.EachYearRet = ''
        self.RollingYearlyRet = ''

    def trans_to_daily_ln_ret(self):
        # 將價格轉換為DailyLnRet
        df = self.adjusted_closed_price_df.copy()
        df = np.log(df).diff(1)
        df.dropna(inplace=True)
        self.DailyLnRet = df

    def cal_to_cum_ln_ret(self):
        # 計算累積報酬率，可搭配lineChart
        df = self.DailyLnRet.copy()
        df = np.exp(df.cumsum()) - 1
        self.DailyCumRet = df

    def cal_each_year_ret(self):
        # 計算每年的報酬率，可搭配BarChart
        df = self.DailyLnRet.copy()
        df['Year'] = pd.DatetimeIndex(df.index).year
        df_group_by_year = np.exp(df.groupby('Year').sum()) - 1
        self.EachYearRet = df_group_by_year

    def cal_rolling_ret(self, m):
        # 計算滾動報酬率，以月資料頻率，並且將報酬率轉為年化，可搭配LineChart
        # 外部參數－m，區間
        df = self.DailyLnRet.copy()
        df['Year'] = pd.DatetimeIndex(df.index).year
        df['Month'] = pd.DatetimeIndex(df.index).month
        df_group_by_ym = df.groupby(['Year', 'Month']).sum()
        df_rolling_yearly_ret = np.exp(df_group_by_ym.rolling(m).sum() * 12 / m) - 1
        df_rolling_yearly_ret.dropna(inplace=True)
        self.RollingYearlyRet = df_rolling_yearly_ret
    # def trans_to_draw_down(self):


def main():
    df = Price.GetInfoFromYM('VNQ AOA SPY', '2010-01-01', '2021-12-31')
    df.get_adjusted_close_price()
    asset_pool = FinancialSeries(df.Result['AdjustedClosedPrice'])
    asset_pool.trans_to_daily_ln_ret()
    asset_pool.cal_to_cum_ln_ret()
    asset_pool.cal_each_year_ret()
    # asset_pool.EachYearRet.plot.bar()
    asset_pool.cal_rolling_ret(72)
    asset_pool.RollingYearlyRet.plot.line()
    plt.show()


main()

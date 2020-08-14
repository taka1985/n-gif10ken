from bs4 import BeautifulSoup
import numpy as np
import pandas as pd
import requests
import tabula
from pandas import DataFrame

def main():
    create_janru_csv()

def get_janru():
    # テーブルの罫線でセルを判定するためのオプションです。 抜き出したい表が罫線で区切られているならlattice=Trueを指定
    # 関数の戻り値：pandas.DataFrameのリスト
    janru_pdfDataFrame = tabula.read_pdf('./dist/pdf/janru.pdf', lattice = True, pages = 'all')
    janru_pdf = pd.concat(janru_pdfDataFrame)
    ds = janru_pdf.iloc[:, :6]
    ds.columns = ['カテゴリ', 'ジャンル', '店舗名', '区', '地域', '取扱商品']
    return ds

# ジャンル
# https://pyhoo.jp/pandas-dataframe-chang#
def create_janru_csv():
    janru_ds = get_janru()
    janru_ds['住所'] = '新潟県新潟市' + janru_ds['区'] + janru_ds['地域']
    janru_ds['区'] =janru_ds['区']
    janru_ds['地域'] =janru_ds['地域']
    janru_ds['カテゴリ(麺類)'] = '0'
 #   ws = ds[ds['取扱商品'].str.contains('酒', na = False)]
 #   ds.loc[ds['取扱商品'].str.contains('酒', na = False),'取扱商品'] = 'aaa'
    janru_ds.loc[janru_ds['ジャンル'].str.contains('中華、ラーメン', na = False), 'カテゴリ(麺類)'] = '1'
    janru_ds.loc[janru_ds['取扱商品'].str.contains('ラーメン', na = False), 'カテゴリ(麺類)'] = '1'
    janru_ds.loc[janru_ds['取扱商品'].str.contains('麵', na = False), 'カテゴリ(麺類)'] = '1'
    janru_ds.loc[janru_ds['取扱商品'].str.contains('パスタ', na = False), 'カテゴリ(麺類)'] = '1'
    janru_ds['カテゴリ(薬局)'] = '0'
    janru_ds.loc[janru_ds['取扱商品'].str.contains('薬', na = False), 'カテゴリ(薬局)'] = '1'
    janru_ds['カテゴリ(衣服)'] = '0'
    janru_ds.loc[janru_ds['取扱商品'].str.contains('洋服', na = False), 'カテゴリ(衣服)'] = '1'
    janru_ds.loc[janru_ds['取扱商品'].str.contains('呉服', na = False), 'カテゴリ(衣服)'] = '1'
    janru_ds.loc[janru_ds['取扱商品'].str.contains('婦人服', na = False), 'カテゴリ(衣服)'] = '1'
    janru_ds['カテゴリ(洋菓子)'] = '0'
    janru_ds.loc[janru_ds['取扱商品'].str.contains('ケーキ', na = False), 'カテゴリ(洋菓子)'] = '1'
    janru_csv = janru_ds[[
        '住所',
        '区',
        '地域',
        'ジャンル',
        '店舗名',
        '取扱商品',
        'カテゴリ',
        'カテゴリ(麺類)',
        'カテゴリ(薬局)',
        'カテゴリ(衣服)',
        'カテゴリ(洋菓子)',
    ]]
    janru_csv.to_csv('dist/csv/janru_csv.csv', index = False)


if __name__ == '__main__':
    main()

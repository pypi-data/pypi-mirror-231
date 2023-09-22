import requests, os
from bs4 import BeautifulSoup
# from 

def test() :
    print('test')

def stock_future_list_main() :

    def _stock_future_list_download(path) :
        # import requests
        # from bs4 import BeautifulSoup
        res = requests.get('http://open.krx.co.kr/contents/OPN/01/01040401/OPN01040401T1.jsp')
        soup = BeautifulSoup(res.content, 'html.parser')
        url = 'http://open.krx.co.kr'
        link = url + soup.find("a", string='주식선물 기초자산 목록')['href']
        res = requests.get(link)
        with open(path, 'wb') as fs: 
            fs.write(res.content)

    def _stock_future_list_prep(path) :
        import pandas as pd
        df = pd.read_excel(path).dropna()
        df.columns = ['_','_','주식선물 종목명','구분','_','기초자산 종목명','_','기초자산 종목코드']
        df = df[['주식선물 종목명','구분','기초자산 종목명','기초자산 종목코드']]
        df['주식선물 종목명'] = df['주식선물 종목명'].str.replace('파생 선물 ', '')
        df['구분'] = df['구분'].str.replace('유가증권','KOSPI')
        df['구분'] = df['구분'].str.replace('코스닥','KOSDAQ')
        df.to_csv(path.replace('(원본).xlsx','(편집).csv'), index=False, encoding='utf-8')

    
    path = 'S:/Dropbox/finance/data/futures/주식선물_기초자산_목록(원본).xlsx'
    _stock_future_list_download(path)
    _stock_future_list_prep(path) 
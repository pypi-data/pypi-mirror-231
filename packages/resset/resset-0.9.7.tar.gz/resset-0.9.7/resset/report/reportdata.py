import requests
import json
from resset.__config import *

def ressetLogin(loginname,loginpwd):
    # login_url=decrypt(loginurl)
    url=loginurl%(loginname,loginpwd)
    # print(url)
    s=requests.get(url).json()
    state=str(s['State'])
    if state=='1':
        print(s['Msg'])
    else:
        print(s['Msg'])
def get_Content_data(code,content_type, type, year):
    # content_url=decrypt(contenturl)
    url=contenturl%(code, content_type,type, year)
    # print(url)
    s=requests.get(url).json()
    state=str(s['State'])
    if state=='1':
        return json.loads(s['Data']) ['response']['docs']
    else:
        print(s['Msg'])

def get_history_data(security,startdate='',enddate=''):
    url=stockurl%(security,startdate,enddate)
    # print(url)
    s=requests.get(url).json()
    state=str(s['State'])
    if state=='1':
        return s['Data']
    else:
        print(s['Msg'])

def get_Income_data(security,startdate='',enddate=''):
    url=incomeurl%(security,startdate,enddate)
    # print(url)
    s=requests.get(url).json()
    state=str(s['State'])
    if state=='1':
        return(s['Data'])
    else:
        print(s['Msg'])

def get_CashFlow_data(security,startdate='',enddate=''):
    url=cashflowurl%(security,startdate,enddate)
    # print(url)
    s=requests.get(url).json()
    state=str(s['State'])
    if state=='1':
        return s['Data']
    else:
        print(s['Msg'])

def get_Balance_data(security,startdate='',enddate=''):
    url=balanceurl%(security,startdate,enddate)
    # print(url)
    s=requests.get(url).json()
    state=str(s['State'])
    if state=='1':
        return s['Data']
    else:
        print(s['Msg'])
if __name__ == '__main__':
    thsLogin = ressetLogin("zhangq", "123")
    s = get_Content_data('GRA', 'part', '10K', '2004')
    print(s)
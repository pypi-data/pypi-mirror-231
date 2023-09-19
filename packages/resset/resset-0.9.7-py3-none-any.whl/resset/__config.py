import pandas as pd
import datetime
from resset.secret import *
#solr地址
# loginurl='x0Bup5R8ha/DkH5559RPCW0r/sNNUqX/EFa/x4sHmQT92BeoBc8/r1gDd1Y29otKHAeb0IFqVvVhU310igs8YFHm3mz1PWXn3ndxAI6dDpA'
# contenturl='x0Bup5R8ha/DkH5559RPCVBWA8Hrn8mylu66nRPCyLBtNmYeUwOSDXCAi46b8EfvOl7avxGNYOQSHl5+yddQoijOKaHar+7+N1ME5cgVqZ4TC1GVFSuuahGOTSM4XkcI'

loginurl='http://39.97.160.135:8092/ressetLogin/Login?loginname=%s&loginpwd=%s'
contenturl='http://39.97.160.135:8092/StockData/Content_data?code=%s&type=%s&tname=%s&year=%s'
stockurl='http://39.97.160.135:8092/StockData/history_data?security=%s&startdate=%s&enddate=%s'
incomeurl='http://39.97.160.135:8092/StockData/Income_data?security=%s&startdate=%s&enddate=%s'
cashflowurl='http://39.97.160.135:8092/StockData/CashFlow_data?security=%s&startdate=%s&enddate=%s'
balanceurl='http://39.97.160.135:8092/StockData/Balance_data?security=%s&startdate=%s&enddate=%s'
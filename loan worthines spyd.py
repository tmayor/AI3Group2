import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from pandas import Series,DataFrame 
from datetime import date
import datetime as DT
import io


#importing the datasets
df1=pd.read_csv('traindemographics.csv')
df2=pd.read_csv('trainperf.csv')
df3=pd.read_csv('trainprevloans.csv')


#merging the datasets
dff=pd.merge(df1,df3, on='customerid', how='left')
dff2=pd.merge(dff,df2, on='customerid', how='left')


#converting datetime for birthdate column to give age
dff2['birthdate'] = dff2['birthdate'].apply('{:10}'.format)
now = pd.Timestamp(DT.datetime.now())
dff2['birthdate'] = pd.to_datetime(dff2['birthdate'], format='%Y-%m-%d %H:%M:%S')    
dff2['birthdate'] = dff2['birthdate'].where(dff2['birthdate'] < now, dff2['birthdate'] -  np.timedelta64(100, 'Y'))   
dff2['age'] = (now - dff2['birthdate']).astype('<m8[Y]')  

#converting datetime differences to integers
appr=dff2['approveddate','']

  
#dropping some redundant columns because weight is less than 50%
#dff2.drop(dff2.columns[[6,8,17,27]], axis=1, inplace=True)








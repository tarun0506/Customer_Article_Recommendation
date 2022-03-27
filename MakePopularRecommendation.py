# -*- coding: utf-8 -*-
"""
Created on Sun Mar 27 19:13:43 2022

@author: Tarun
"""

import pandas as pd

df_customer_all=pd.read_csv('data/customers.csv')
df_transaction_all_records=pd.read_csv('data/transactions_train.csv')
no_history_customer_list=set(df_customer_all['customer_id'])-set(df_transaction_all_records['customer_id'])
df_customer_all['age_bins'] = pd.cut(x=df_customer_all['age'], bins=[0,18, 25, 35, 45,60,90],labels=[1,2,3,4,5,6])
customer='3bcbec94fd936669b6f09c5964bc0ceb3b1b79b8469de8751941a80ee9da30be'
if customer in no_history_customer_list :
    age_bin=df_customer_all[df_customer_all['customer_id']=='fffef3b6b73545df065b521e19f64bf6fe93bfd450ab20e02ce5d1e58a8f700b']['age_bins'].iloc[0]
    custlist=df_customer_all[df_customer_all['age_bins']==age_bin]['customer_id'].unique()
    print(df_transaction_all_records[df_transaction_all_records['customer_id'].isin(custlist)].groupby(['article_id']).size().head(12))
    
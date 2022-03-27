# -*- coding: utf-8 -*-
"""
Created on Sun Mar 27 17:22:52 2022

@author: Tarun
"""


'''
Creating indexes for both customers and articles.
Advantage is faster retrival of records and faster preprocessing
It reduces the dataset size as well for both customer and article ids
'''
import pandas as pd
import numpy as np
def createIndexes():
    '''
    df_transactions=pd.read_csv('data/transactions_train.csv')
    df_transactions=df_transactions[['article_id', 'customer_id']]
    df_transactions_frequency=df_transactions.groupby(["article_id", "customer_id"]).size().reset_index(name="Count")    
    df_transactions_frequency.to_csv('preprocess/df_transactions_frequency.csv',index=False)
    '''
    #uncomment above lines to generate it again
    df_transactions_frequency=pd.read_csv('preprocess/df_transactions_frequency.csv')
    articledict={}
    count=0
    for article in df_transactions_frequency['article_id'].unique():
      articledict[article]=count
      count+=1
    customerdict={}
    count=0
    for article in df_transactions_frequency['customer_id'].unique():
      customerdict[article]=count
      count+=1
    df_transactions_frequency['article_id']=df_transactions_frequency['article_id'].map(articledict) 
    df_transactions_frequency['customer_id']=df_transactions_frequency['customer_id'].map(customerdict)
    dict2Article = {v: k for k, v in articledict.items()}
    print('saving article dictionary..')
    np.save("preprocess/dict2Article.npy",dict2Article)
    dict2Customer = {v: k for k, v in customerdict.items()}
    print('saving customer dictionary..')
    np.save("preprocess/dict2Customer.npy",dict2Customer)
    print('saving indexed dataset..')
    df_transactions_frequency.to_csv("preprocess/Transactions_Train_Index.csv",index=False)
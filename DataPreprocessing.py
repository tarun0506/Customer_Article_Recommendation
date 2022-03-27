# -*- coding: utf-8 -*-
"""
Created on Sun Mar 27 17:54:28 2022

@author: Tarun
"""

'''
Proprocessing is being done for Item to Item Based Collaborative Filtering

Converting all customers as columns, articles as rows and no of times customer purchased the article is it's value

Tested for smaller dataset,however this code works for all the customers and articles with data distribution and parallel processing 
Please feel free to change max_customers and max_articles
'''
import pandas as pd
import numpy as np

def data_preprocessing():
    max_customers=1000
    max_articles=30
    df_transactions_frequency_index=pd.read_csv('preprocess/Transactions_Train_Index.csv')
    transactions_array=df_transactions_frequency_index.values
    df=pd.DataFrame(columns=[x for x in range(0,max_customers)])
    
    
    def process_articles_customers(item):
        df_article=transactions_array[transactions_array[:,0]==item]
        print(item)
        input=[]
        input1 = [df_article[df_article[:,1]==i][0][2]  if len(df_article[df_article[:,1]==i])>0  else 0 for i in range(0,max_customers)]       
        arr=np.array(input1).reshape(1,-1)
        #df=df.append(pd.DataFrame(arr.reshape(1,-1), columns=list(df)), ignore_index=True)
        return arr
    array_list = [process_articles_customers(item) for item in range(0,max_articles)] 
    df=df.append(pd.DataFrame(np.concatenate(array_list,axis=0), columns=list(df)), ignore_index=True)  
    df.to_csv('preprocess/Article_Customer_Matrix.csv')
# -*- coding: utf-8 -*-
"""
Created on Sun Mar 27 18:14:09 2022

@author: Tarun
"""

import pandas as pd
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
df_preprocessed_dataset=pd.read_csv('preprocess/Article_Customer_Matrix.csv')
df_preprocessed_dataset_array=np.array(df_preprocessed_dataset)

def item_similarity(item1,item2):
    item1_array=df_preprocessed_dataset_array[item1,1:]
    item2_array=df_preprocessed_dataset_array[item2,1:]
    #print(item1_array)
    #print(item2_array)
    cs = cosine_similarity(item1_array.reshape(1,-1),item2_array.reshape(1,-1))
    return cs[0][0]

def unique_items():
    unique_items_list = []
    s=set(np.unique(df_preprocessed_dataset_array[:,0]))
    unique_items_list=list(s)
    return unique_items_list
unique_items()

#print(item_similarity(8,9))
#print(item_similarity(27,9))
#print(item_similarity(27,6))

def most_similar_items(target_item):
    un_lst=unique_items()
    scores = [(item_similarity(target_item,other_item),str(target_item)+" --> "+str(other_item)) for other_item in un_lst if other_item!=target_item]
    scores.sort(reverse=True)
    return scores
#print(most_similar_items(9))
def target_item_to_customers(target_customers):
    target_customers_articles_lst = []
    unique_list =unique_items()
    for article in np.unique(np.where(df_preprocessed_dataset_array[:,9+1]>0)):
        target_customers_articles_lst.append(article)

    s=set(unique_list)
    recommended_articles=list(s.difference(target_customers_articles_lst))
    a = len(recommended_articles)
    if a == 0:
        return 0
    return recommended_articles,target_customers_articles_lst
#unpurchased_articles,parchased_articles=target_item_to_customers(9)
def recommendation_phase(target_customer):
    unpurchased_articles,parchased_articles=target_item_to_customers(target_customer)
    #seen_ratings = [[dataset[target_person][movies],movies] for movies in dataset[target_person]]
    #weighted_avg,weighted_sim = 0,0
    if not parchased_articles:
        print('No articles purchased by customer')
    rankings =[]
    for unparchased_article in unpurchased_articles:
        for article in parchased_articles:
            item_sim=item_similarity(unparchased_article,article)           
            rankings.append([item_sim,unparchased_article,article])
    rankings.sort(reverse=True)
    return rankings
def getRecommendations(customerList):
    Customer2dict=np.load("preprocess/dict2Customer.npy",allow_pickle=True).item()
    dict2Customer = {v: k for k, v in Customer2dict.items()}
    print("Enter the target customer")
    #tp = input().title()
    #
    for cust in customerList:
        recommendations=[]
        
        a=recommendation_phase(cust)
            
        for w,m,n in a:
                    #print(m," ---> ",n,"--->with",w)
                    if m not in recommendations :
                        recommendations.append(m)
                    if len(recommendations)==12:
                        break
        recommendations            
        dict2Article=np.load("preprocess/dict2Article.npy",allow_pickle=True).item()
        print("Your recommeded items for customer ",cust," are")
        print([dict2Article.get(article,'') for article in recommendations])
        
            
            
            
            
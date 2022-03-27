# -*- coding: utf-8 -*-
"""
Created on Sun Mar 27 17:18:41 2022

@author: Tarun
"""
'''
# Considered different recommendation approaches:
1) Content based recommendation
2) Collaborative Filtering
3) Item to Item Based Collaborative Filtering

1) Content based Recommendation:
Recommending articles similar to customer purchased items

Disadvantage:
It can only recommend based on the existing interest of the customer and has limited ability to expand on existing interests.


2) Collaborative Filtering:
We find similar customers and recommend items purchased by similar customers

Disadvantages:
Algorithm is restricted to similar customers and their purchased articles. This is computationally expensive because it is O(MN) in the worst case, M is the number of customers and N is the number of items.

3) Item to Item base Collaborative Filtering(Our Approach)

Instead of matching the customer to similar customers, item-to-item collaborative filtering matches each of the customer's purchased items to similar items, then combines those similar items into a recommendation list

Example: If a person A purchased item 1,item 2 and item 3, person B purchased item 1 and item 2. Then our algorithm recommend item 2 to the person B
Advantages:
Algorithm produces highly correlated similar items with high recommendation quality.
Disadvantages:
This is also computationally expensive O(NM) in the worst case, M is the number of customers and N is the number of items
'''


from DataIndexing import createIndexes
from DataPreprocessing import data_preprocessing
from ItemToItemCollaborativeFiltering import getRecommendations
import numpy as np
#Uncomment to create indexes again
#createIndexes()
#data_preprocessing()
customerPredictionList=['001Ae5408A043F64Bccd32Beffe2730151414Cbdf18A6Eb3Cc8D30Bdca605652','0022a721371d5949d174ecba60346d89a9d6c08c0fba4f47b3b1e66b3fb58fd8']
getRecommendations(customerPredictionList)
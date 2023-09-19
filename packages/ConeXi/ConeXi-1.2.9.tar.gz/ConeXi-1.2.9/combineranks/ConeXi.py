# -*- coding: utf-8 -*-
"""
Created on Mon Jan 23 10:33:40 2023

@author: Jose Ribeiro


"""

import pandas as pd

class ConeXi():
    
    def __init__(self, top_n_rank):
        self.top_n_rank = top_n_rank
    
        
    def ExecuteConeXi(self, df_features_rank):
        df_features_rank_copy = df_features_rank.copy()
        df_features_rank_step1 = df_features_rank.copy()
        features = list(df_features_rank_copy['att_original_names']) #column names of experts/measures
        features_w = list(df_features_rank_copy['weights']) #weights for each expert/measure.
        col = list(df_features_rank_copy.columns)
        col.remove('att_original_names')
        col.remove('weights')
        
        for idl,l in enumerate(features):
          for idc,c in enumerate(col):
            for idp,p in enumerate(df_features_rank_copy.loc[:,c]):
              if l == p:
                if idp < self.top_n_rank:
                  df_features_rank_step1.loc[idl,c] = idp+1
                else:
                  df_features_rank_step1.loc[idl,c] = 0
        
        
        df_step_1 = df_features_rank_step1.copy()
        
        df_features_rank_step1 = df_features_rank_step1.set_index('att_original_names')
        
            
        # initialize data of lists.
        data = {}
        
        # Creates pandas DataFrame.
        df = pd.DataFrame(data, index=df_features_rank_step1.index)
        
        for idl,l in enumerate(features):
          #if idl < self.top_n_rank:
              s_line = 0
              for idc,c in enumerate(col):
                for i in range(self.top_n_rank):
                  if df_features_rank_step1.loc[l,c] <= i+1 and df_features_rank_step1.loc[l,c] != 0:
                    s_line += 1 
              df.loc[l,'S'] = s_line * features_w[idl]
        
        df_final = df.sort_values('S',ascending=False)
        return df_final, df_step_1
    
def main():
    
    #Simple example of utilization of ConeXi
    
    d = {'att_original_names':  ['A', 'B','C','D','E','F','G'], 
                    'weights':  [ 1 , 1 , 1 , 1  , 1 , 1 , 1 ],
                     'Rank_1':  ['A', 'B','C','D','E','F','G'], 
                     'Rank_2':  ['A', 'B','D','C','G','E','F'],
                     'Rank_3':  ['A', 'C','B','F','D','E','G' ]}
    
    
    df = pd.DataFrame(data=d)
    df.reset_index()
    
    c = ConeXi(4)
    
    rank_final, data = c.ExecuteConeXi(df)
    
    print("Intermediate table:")
    print(data)
    print()
    print("Final rank:")
    print(rank_final)
    
if __name__ == "__main__":
    main()

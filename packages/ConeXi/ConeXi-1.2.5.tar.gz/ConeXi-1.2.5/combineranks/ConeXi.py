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
                for i,_ in enumerate(features):
                  if df_features_rank_step1.loc[l,c] <= i+1: #and df_features_rank_step1.loc[l,c] != -1:
                    s_line += 1 
              df.loc[l,'S'] = s_line * features_w[idl]
        
        df_final = df.sort_values('S',ascending=False)
        return df_final, df_step_1
    
def main():
    
    #Simple example of utilization of ConeXi
    
    #d = {'att_original_names': ['A', 'B','C','D'], 
    #                'weights': [ 1 , 1 , 1 , 1  ],
    #                 'Rank_1':  ['A', 'B','C','D'],
    #                 'Rank_2':  ['A','C','B','D' ],
    #                 'Rank_3':  ['A','B','C','D' ]}
    
    d = {'att_original_names': ['mes_num_crb',
                                 'quant_lesao_corporal_crb',
                                 'quant_ameaca_crb',
                                 'quant_roubo_crb',
                                 'quant_injuria_crb',
                                 'quant_furto_crb',
                                 'quant_lesao_no_transito_crb',
                                 'quant_dano_no_transito_crb',
                                 'quant_difamacao_crb',
                                 'quant_homicidio_crb',
                                 
                                 'quant_abandono_do_lar_crb',
                                 'quant_conflitos_vicinais_crb',
                                 'quant_conflitos_conjugais_crb',
                                 'quant_fuga_do_lar_crb',
                                 'quant_estupro_de_vulneravel_crb',
                                 'quant_outros_fatos_atipicos_crb',
                                 'quant_roubo_de_veiculo_crb',
                                 'quant_estelionato_crb',
                                 'quant_dano_crb',
                                 'quant_dano_civil_crb',
                                 'quant_calunia_crb',
                                 'quant_conflitos_familiares_crb',
                                 'quant_trafico_de_drogas_crb',
                                 'quant_vias_de_fato_crb',
                                 'quant_apropriacao_indebita_crb',
                                 'quant_agressao_fisica_crb',
                                 'quant_receptacao_crb',
                                 'quant_estupro_crb',
                                 'quant_desaparecimento_de_pessoa_crb',
                                 'quant_tentativa_de_homicidio_crb',
                                 'quant_poluicao_sonora_crb',
                                 'quant_outras_fraudes_crb',
                                 'quant_desobediencia_crb',
                                 'quant_desacato_crb',
                                 'quant_perturbacoes_da_tranquilidade_crb'], 
                    'weights': [ 1 , 1 , 1 , 1 , 1, 1, 1, 1, 1, 1,
                                1 , 1 , 1 , 1 , 1, 1, 1, 1, 1, 1,
                                1 , 1 , 1 , 1 , 1, 1, 1, 1, 1, 1,
                                1,1,1,1,1],
                     'Rank_1':  ['quant_ameaca_crb',
                                 'quant_lesao_corporal_crb',
                                 'quant_roubo_crb',
                                 'quant_homicidio_crb',
                                 'quant_dano_no_transito_crb',
                                 'quant_abandono_do_lar_crb',
                                 'quant_outros_fatos_atipicos_crb',
                                 'quant_trafico_de_drogas_crb',
                                 'quant_vias_de_fato_crb',
                                 'quant_injuria_crb',
                                 'quant_conflitos_familiares_crb',
                                 'quant_furto_crb',
                                 'quant_calunia_crb',
                                 'quant_estelionato_crb',
                                 'quant_apropriacao_indebita_crb',
                                 'quant_difamacao_crb',
                                 'quant_agressao_fisica_crb',
                                 'quant_roubo_de_veiculo_crb',
                                 'quant_lesao_no_transito_crb',
                                 'quant_dano_crb',
                                 'quant_dano_civil_crb',
                                 'quant_conflitos_conjugais_crb',
                                 'quant_estupro_crb',
                                 'quant_desaparecimento_de_pessoa_crb',
                                 'quant_poluicao_sonora_crb',
                                 'quant_fuga_do_lar_crb',
                                 'quant_desobediencia_crb',
                                 'mes_num_crb',
                                 'quant_tentativa_de_homicidio_crb',
                                 'quant_estupro_de_vulneravel_crb',
                                 'quant_receptacao_crb',
                                 'quant_desacato_crb',
                                 'quant_conflitos_vicinais_crb',
                                 'quant_outras_fraudes_crb',
                                 'quant_perturbacoes_da_tranquilidade_crb'],
                     'Rank_2':  ['mes_num_crb',
                                 'quant_homicidio_crb',
                                 'quant_tentativa_de_homicidio_crb',
                                 'quant_roubo_crb',
                                 'quant_roubo_de_veiculo_crb',
                                 'quant_desaparecimento_de_pessoa_crb',
                                 'quant_ameaca_crb',
                                 'quant_conflitos_vicinais_crb',
                                 'quant_estupro_crb',
                                 'quant_agressao_fisica_crb',
                                 'quant_abandono_do_lar_crb',
                                 'quant_apropriacao_indebita_crb',
                                 'quant_calunia_crb',
                                 'quant_conflitos_conjugais_crb',
                                 'quant_conflitos_familiares_crb',
                                 'quant_dano_civil_crb',
                                 'quant_dano_crb',
                                 'quant_dano_no_transito_crb',
                                 'quant_desacato_crb',
                                 'quant_desobediencia_crb',
                                 'quant_difamacao_crb',
                                 'quant_estelionato_crb',
                                 'quant_estupro_de_vulneravel_crb',
                                 'quant_fuga_do_lar_crb',
                                 'quant_furto_crb',
                                 'quant_injuria_crb',
                                 'quant_lesao_corporal_crb',
                                 'quant_lesao_no_transito_crb',
                                 'quant_outras_fraudes_crb',
                                 'quant_outros_fatos_atipicos_crb',
                                 'quant_perturbacoes_da_tranquilidade_crb',
                                 'quant_poluicao_sonora_crb',
                                 'quant_receptacao_crb',
                                 'quant_trafico_de_drogas_crb',
                                 'quant_vias_de_fato_crb'],
                     'Rank_3':  ['quant_outros_fatos_atipicos_crb',
                                 'quant_conflitos_conjugais_crb',
                                 'quant_roubo_crb',
                                 'quant_outras_fraudes_crb',
                                 'quant_agressao_fisica_crb',
                                 'quant_abandono_do_lar_crb',
                                 'quant_furto_crb',
                                 'quant_receptacao_crb',
                                 'quant_lesao_corporal_crb',
                                 'quant_estupro_de_vulneravel_crb',
                                 'quant_fuga_do_lar_crb',
                                 'quant_desacato_crb',
                                 'quant_estupro_crb',
                                 'quant_apropriacao_indebita_crb',
                                 'quant_calunia_crb',
                                 'quant_roubo_de_veiculo_crb',
                                 'quant_perturbacoes_da_tranquilidade_crb',
                                 'quant_homicidio_crb',
                                 'quant_conflitos_familiares_crb',
                                 'quant_vias_de_fato_crb',
                                 'quant_desaparecimento_de_pessoa_crb',
                                 'quant_injuria_crb',
                                 'quant_trafico_de_drogas_crb',
                                 'quant_lesao_no_transito_crb',
                                 'quant_ameaca_crb',
                                 'quant_conflitos_vicinais_crb',
                                 'quant_difamacao_crb',
                                 'quant_poluicao_sonora_crb',
                                 'quant_estelionato_crb',
                                 'quant_desobediencia_crb',
                                 'quant_dano_crb',
                                 'quant_tentativa_de_homicidio_crb',
                                 'quant_dano_no_transito_crb',
                                 'quant_dano_civil_crb',
                                 'mes_num_crb']}
    
    df = pd.DataFrame(data=d)
    df.reset_index()
    
    c = ConeXi(10)
    
    rank_final, data = c.ExecuteConeXi(df)
    
    print("Intermediate table:")
    print(data)
    print()
    print("Final rank:")
    print(rank_final)
    
if __name__ == "__main__":
    main()

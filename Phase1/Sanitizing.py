import pandas as pd
import random as rd
import numpy as np



# ------------------SECÇÃO RESPONSAVEL PELO CORTE DO DATASET ORIGINAL--------------------------------------

def cut_dataset():
    df = pd.read_csv("adult.csv", nrows=6500)   # lê só as primeiras 6500 linhas de dados
    return df
#-------------------------------------------------------------


#------------------SECÇÃO RESPONSAVEL PELA VARIEDADE DE INCOME NO DATASET--------------------------------------
def generate_income(income_class):
    if income_class == '<=50K':
        val = np.random.lognormal(mean=10.37, sigma=0.4)
        return int(np.clip(val, 15000, 50000))
    else:
        val = np.random.lognormal(mean=11.2, sigma=0.5)
        return int(np.clip(val, 50001, 250000))
    
#--------------------------------------------------------------



#------------------SECÇÃO RESPONSAVEL PELA RESOLUCAO DE DADOS EM FALTA NO DATASET--------------------------------------
def missing_data(df):

    col_num = df.shape[1]  # número de colunas do dataset

    for i in range(col_num):
        for j in range(df.iloc[:, i].shape[0]):
            if (df.iloc[j,i] == '?'):  # verifica se o valor da célula é igual a '?'
                df.iloc[j,i] = df.iloc[j-1,i] # substitui o valor da célula pelo valor anterior


    return df


#-----------------------ELIMINÇÃO DE COLUNAS INUTEIS E DADOS 100% CORRELATED---------------------------------------
"""Foram eliminadas as colunas correspondentes a fnlwgt e education, 
pois a primeira não tem relevância para o dataset e a segunda é 100% 
correlacionada com a coluna education-num"""
def remove_columns(df):

    first_line = np.array(df.columns)  # seleciona a primeira linha do dataset

    matrix_data = np.array(df)  # converte o dataframe em uma matriz numpy
    matrix_data = np.delete(matrix_data,[2,3], axis=1)  # remove a coluna 2 e 3 (fnlwgt e education) da matriz
    first_line = np.delete(first_line,[2,3])  # remove os nomes das colunas 2 e 3 da primeira linha

    df = pd.DataFrame(matrix_data)  # converte a matriz de volta para um dataframe
    df.columns = first_line  # atribui os nomes das colunas da primeira linha

    return df


if __name__ == "__main__":

    df = cut_dataset()

    df['income'] = df.iloc[:, -1].apply(generate_income)

    df = missing_data(df)

    df = remove_columns(df)

    df.to_csv("limited_data.csv", index=False)  # salva o dataset

    df = df.drop_duplicates() # Evita duplicados

    df.to_csv("limited_data.csv", index=False)  # salva o dataset
#--------------------------------------------------------------

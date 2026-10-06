import pandas as pd
import random as rd


# ------------------SECÇÃO RESPONSAVEL PELO CORTE DO DATASET ORIGINAL--------------------------------------
"""
df = pd.read_csv("adult.csv", nrows=6500)   # lê só as primeiras 6500 linhas de dados
df.to_csv("limited_data.csv", index=False)
"""
#-------------------------------------------------------------

#------------------SECÇÃO RESPONSAVEL PELA VARIEDADE DE INCOME NO DATASET--------------------------------------
"""
df = pd.read_csv("limited_data.csv")

income_col = [rd.randint(40000, 80000) for _ in range(df.iloc[:, -1].shape[0])]  # cria uma lista de valores aleatórios entre 40000 e 80000 com o mesmo tamanho da coluna income
df.iloc[:, -1] = income_col  # substitui a coluna income pelos valores aleatórios gerados
df.to_csv("limited_data.csv", index=False)  # salva o dataset
"""
#--------------------------------------------------------------

#------------------SECÇÃO RESPONSAVEL PELA RESOLUCAO DE DADOS EM FALTA NO DATASET--------------------------------------

df = pd.read_csv("limited_data.csv")

col_num = df.shape[1]  # número de colunas do dataset

for i in range(col_num):
    for j in range(df.iloc[:, i].shape[0]):
        if (df.iloc[j,i] == '?'):  # verifica se o valor da célula é igual a '?'
            df.iloc[j,i] = df.iloc[j-1,i] # substitui o valor da célula pelo valor anterior

df.to_csv("limited_data.csv", index=False)  # salva o dataset
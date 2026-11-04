import pandas as pd
import random




if __name__ == "__main__":
    df = pd.read_csv("Dataset.csv")  

    start = 0
    size = 5000

    for i in range(0, 5):
        df1 = df.iloc[start:start+size]  # seleciona um subconjunto do dataset

        start += size - int(0.1 * size)  # atualiza o índice inicial para o próximo subconjunto. Garante overlap de 10% entre os subconjuntos
        size = random.randint(5000, 10000)  # gera um novo tamanho aleatório para o próximo subconjunto

        df1.to_csv(f"Dataset_{i}.csv", index=False)  # salva o dataset embaralhado em um novo arquivo CSV

from numpy import size
import pandas as pd




if __name__ == "__main__":
    df = pd.read_csv("Dataset.csv")  

    start = 0
    sizes = [5000, 7500, 10000, 12500, 15000]  # Tamanhos únicos para cada par


    for i in range(5):
        # 1. Gera o tamanho único para o par atual
        size = sizes[i]
        print(f"Tamanho do par {i}: {size}")

        step = size - int(0.1 * size)  # Deslocamento considerando 10% de overlap

        # 2. Dataset A do par
        df_a = df.iloc[start : start + size]
        start += step  # Avança mantendo 10% de overlap para o B

        # 3. Dataset B do par (com o MESMO tamanho do Dataset A)
        df_b = df.iloc[start : start + size]
        start += step  # Avança para o próximo par (overlap também permitido aqui)

        # 4. Salva os arquivos do par
        df_a.to_csv(f"Dataset_{i}_A.csv", index=False)
        df_b.to_csv(f"Dataset_{i}_B.csv", index=False)
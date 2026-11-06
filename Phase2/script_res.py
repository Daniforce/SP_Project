import subprocess
import time
import pandas as pd

NUM_PARES = 5
EXECUCOES_POR_PAR = 5
PROTOCOLO = "0"  # 0: Naive Hashing | 1: Server-Aided | 2: Diffie-Hellman | 3: OT-based

# Caminho apontando duas pastas atrás (use "../../demo" no Linux se não tiver extensão .exe)
PATH_DEMO = "../../demo.exe"

resultados = []

for i in range(NUM_PARES):
    arq_a = f"Dataset_{i}_A.csv"
    arq_b = f"Dataset_{i}_B.csv"

    # Executável apontando para duas pastas acima
    cmd_srv = [PATH_DEMO, "-r", "0", "-p", PROTOCOLO, "-f", arq_a]
    cmd_cli = [PATH_DEMO, "-r", "1", "-p", PROTOCOLO, "-f", arq_b]

    tempos_par = []
    elementos_comuns = 0

    print(f"--- Processando Par {i} com Protocolo {PROTOCOLO} ({arq_a} vs {arq_b}) ---")

    for run in range(EXECUCOES_POR_PAR):
        inicio = time.perf_counter()

        # Inicia o Servidor (Role 0)
        p_srv = subprocess.Popen(cmd_srv, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        time.sleep(0.1)  # Aguarda a abertura do socket

        # Inicia o Cliente (Role 1)
        p_cli = subprocess.Popen(cmd_cli, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

        # Aguarda a conclusão dos dois processos
        out_cli, _ = p_cli.communicate()
        p_srv.communicate()

        fim = time.perf_counter()
        duracao = fim - inicio
        tempos_par.append(duracao)

        if run == 0 and out_cli:
            elementos_comuns = len(out_cli.decode().strip().splitlines())

        print(f"  Execução {run + 1}/{EXECUCOES_POR_PAR}: {duracao:.4f} s")

    tempo_medio = sum(tempos_par) / len(tempos_par)
    print(f"-> Tempo médio do Par {i}: {tempo_medio:.4f} s\n")

    resultados.append({
        "Par": i,
        "Protocolo": PROTOCOLO,
        "Ficheiro A": arq_a,
        "Ficheiro B": arq_b,
        "Tempo Médio (s)": round(tempo_medio, 4),
        "Elementos Comuns": elementos_comuns
    })

# Exibe o resumo no terminal e salva em CSV
df_res = pd.DataFrame(resultados)
print("=== RESULTADOS DAS EXECUÇÕES ===")
print(df_res.to_string(index=False))

df_res.to_csv("resultados_execucao.csv", index=False)

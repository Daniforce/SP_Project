import re
import subprocess
import tempfile
import time
import pandas as pd

NUM_PARES = 5
EXECUCOES_POR_PAR = 5
PROTOCOLO = "2"  # 0: Naive, 1: Server-Aided (3 partes), 2: DH-PSI (2 partes), 3: OT-PSI (2 partes)
PATH_DEMO = "../../demo.exe"
IP_LOCAL = "127.0.0.1"

resultados = []

for i in range(NUM_PARES):
    arq_a = f"Dataset_{i}_A.csv"
    arq_b = f"Dataset_{i}_B.csv"

    print(f"--- Processando Par {i} com Protocolo -p {PROTOCOLO} ({arq_a} vs {arq_b}) ---")
    tempos_par = []
    elementos_comuns = 0

    for run in range(EXECUCOES_POR_PAR):
        if PROTOCOLO == "1":
            # --- PROTOCOLO -p 1 (Server-Aided: 3 partes) ---
            cmd_srv   = [PATH_DEMO, "-r", "0", "-p", "1", "-f", arq_a, "-a", IP_LOCAL]
            cmd_cli_a = [PATH_DEMO, "-r", "1", "-p", "1", "-f", arq_a, "-a", IP_LOCAL]
            cmd_cli_b = [PATH_DEMO, "-r", "1", "-p", "1", "-f", arq_b, "-a", IP_LOCAL]

            with tempfile.TemporaryFile(mode="w+") as f_cli_a, \
                 tempfile.TemporaryFile(mode="w+") as f_cli_b:

                p_srv = subprocess.Popen(cmd_srv, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
                time.sleep(0.05)
                p_cli_a = subprocess.Popen(cmd_cli_a, stdout=f_cli_a, stderr=subprocess.STDOUT, text=True)
                time.sleep(0.05)

                inicio = time.perf_counter()
                p_cli_b = subprocess.Popen(cmd_cli_b, stdout=f_cli_b, stderr=subprocess.STDOUT, text=True)

                p_cli_a.wait(timeout=60)
                p_cli_b.wait(timeout=60)
                fim = time.perf_counter()

                if p_srv.poll() is None:
                    p_srv.terminate()
                    p_srv.wait()

                f_cli_a.seek(0)
                f_cli_b.seek(0)
                out_total = f_cli_a.read() + "\n" + f_cli_b.read()

        else:
            # --- PROTOCOLOS DE 2 PARTES (-p 0, -p 2, -p 3) ---
            cmd_srv = [PATH_DEMO, "-r", "0", "-p", PROTOCOLO, "-f", arq_a]
            cmd_cli = [PATH_DEMO, "-r", "1", "-p", PROTOCOLO, "-f", arq_b]

            p_srv = subprocess.Popen(cmd_srv, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
            time.sleep(0.1)

            inicio = time.perf_counter()
            p_cli = subprocess.Popen(cmd_cli, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
            out_cli, _ = p_cli.communicate(timeout=60)
            p_srv.wait(timeout=5)
            fim = time.perf_counter()

            out_total = out_cli or ""

        duracao = fim - inicio
        tempos_par.append(duracao)

        if run == 0 and out_total:
            match = re.search(r"Found\s+(\d+)\s+intersecting elements", out_total)
            if match:
                elementos_comuns = int(match.group(1))

        print(f"  Execução {run + 1}/{EXECUCOES_POR_PAR}: {duracao:.4f} s")

    tempo_medio = sum(tempos_par) / len(tempos_par)
    print(f"-> Tempo médio do Par {i}: {tempo_medio:.4f} s | Elementos em comum: {elementos_comuns}\n")

    resultados.append({
        "Par": i,
        "Protocolo": PROTOCOLO,
        "Ficheiro A": arq_a,
        "Ficheiro B": arq_b,
        "Tempo Médio (s)": round(tempo_medio, 4),
        "Elementos Comuns": elementos_comuns
    })

df_res = pd.DataFrame(resultados)
print("=== RESULTADOS FINAIS ===")
print(df_res.to_string(index=False))

df_res.to_csv("resultados_execucao.csv", index=False)

import time

from tqdm import tqdm

# Número total de iterações
total_iteracoes = 100

# Crie uma barra de carregamento usando tqdm
for i in tqdm(range(total_iteracoes), desc="Processando", ncols=100):
    # Simule uma tarefa demorada
    time.sleep(0.1)

print("Tarefa concluída!")
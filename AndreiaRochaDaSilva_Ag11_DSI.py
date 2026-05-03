import colorama
from colorama import Fore, Style
import random


colorama.init(autoreset=True)

def monitorar_reservatorio(nivel):
    """
    Função exigida: define a cor e a mensagem conforme o nível.
    """
    
    mensagens = [
        "Muito baixo (crítico)", # Nível 1
        "Baixo",                # Nível 2
        "Médio",                # Nível 3
        "Alto",                 # Nível 4
        "Muito alto (alerta)"   # Nível 5
    ]
    
   
    cores = [Fore.RED, Fore.YELLOW, Fore.GREEN, Fore.CYAN, Fore.BLUE]

    # Ajuste do índice (níveis 1-5 para índices 0-4)
    indice = nivel - 1
    
    print(f"Nível detectado: {nivel}")
    print(cores[indice] + f"Situação: {mensagens[indice]}")
    print("-" * 30)


opcoes_niveis = [1, 2, 3, 4, 5]

# Random.choice para selecionar um nível da lista de forma aleatória
nivel_aleatorio = random.choice(opcoes_niveis)

monitorar_reservatorio(nivel_aleatorio)
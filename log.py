import sys
from time import sleep

def loading_bar(duration):
    """Função para mostrar uma barra de carregamento simples."""
    total = 20  # Número de etapas na barra de carregamento
    step = duration / total
    for i in range(total + 1):
        sys.stdout.write("\r[{}{}] {:.0f}%".format('#' * i, '-' * (total - i), (i / total) * 100))
        sys.stdout.flush()
        sleep(step)
    sys.stdout.write("\n")
    sys.stdout.flush()
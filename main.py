import random

dardos = 10_000_000
acertos = 0
tamanho_barra = 40 


for i in range(dardos):
    x = random.random()
    y = random.random()
    teorema = (x**2 + y**2)
    if teorema <= 1:
        acertos += 1

    if i % 50000 == 0 or i == dardos - 1:
        progresso = i / dardos
        bloquinhos = int(tamanho_barra * progresso) 

        desenho = '█' * bloquinhos + '-' * (tamanho_barra - bloquinhos)
        print(f'\r[{desenho}] {progresso:.1%} de dardos atirados...', end='', flush=True)

print("\n")
fim = (acertos/dardos)*4
print(fim)

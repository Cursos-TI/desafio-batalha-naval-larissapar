import random

# Tamanho do tabuleiro
tamanho = 5
tabuleiro = [["~"] * tamanho for _ in range(tamanho)]

# Posição aleatória do navio
linha_navio = random.randint(0, tamanho - 1)
coluna_navio = random.randint(0, tamanho - 1)

print("Bem-vindo ao jogo Batalha Naval!")
print("O tabuleiro tem tamanho 5x5. Tente adivinhar a posição do navio!")

# Jogador tem 5 tentativas
for tentativa in range(5):
print("\nTentativa", tentativa + 1)
for linha in tabuleiro:
print(" ".join(linha))

linha = int(input("Escolha a linha (0-4): "))
coluna = int(input("Escolha a coluna (0-4): "))

if linha == linha_navio and coluna == coluna_navio:
print("Parabéns! Você acertou o navio!")
tabuleiro[linha][coluna] = "X"
break
else:
print("Errou! O navio não está aí.")
tabuleiro[linha][coluna] = "O"

print("\nFim de jogo! O navio estava na posição:", linha_navio, coluna_navio)

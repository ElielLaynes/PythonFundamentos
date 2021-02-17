# Hangman Game (Jogo da Forca)
# Programação Orientada a Objetos

# Import
import random

# Board (tabuleiro) -> "corpo do jogo", é onde vai aparecer a forca se formando
corpo = ['''

>>>>>>>>>>Jogo da Forca<<<<<<<<<<

+---+
|   |
    |
    |
    |
    |
=========''', '''

+---+
|   |
O   |
    |
    |
    |
=========''', '''

+---+
|   |
O   |
|   |
    |
    |
=========''', '''

 +---+
 |   |
 O   |
/|   |
     |
     |
=========''', '''

 +---+
 |   |
 O   |
/|\  |
     |
     |
=========''', '''

 +---+
 |   |
 O   |
/|\  |
/    |
     |
=========''', '''

 +---+
 |   |
 O   |
/|\  |
/ \  |
     |
=========''']


# Classe
class enforcado:

	# Método Construtor
	def __init__(self, palavra):
		self.palavra = palavra
		self.letra_errada = []
		self.letra_certa = []
		print('classe inicidada')
		
	# Método para adivinhar a letra
	def adivinhar(self, letra):
		if letra in self.palavra and letra not in self.letra_certa:
			self.letra_certa.append(letra)
		elif letra not in self.palavra and letra not in self.letra_errada:
			self.letra_errada.append(letra)
		else:
			return False
		return True
		
	# Método para verificar se o jogo terminou
	def jogo_terminou(self):
		return self.jogador_venceu() or (len(self.letra_errada) == 6)
		
	# Método para verificar se o jogador venceu
	def jogador_venceu(self):
		if '_' not in self.esconder_palavra():
			return True
		return False

	# Método para não mostrar a letra da palavra correta no board
	def esconder_palavra(self):
		lc = ''
		for letra in self.palavra:
			if letra not in self.letra_certa:
				lc += ' '
			else:
				lc += letra
		return lc
		
	# Método para checar o status do game e imprimir o board na tela
	def print_status_jogo(self):
		print(corpo[len(self.letra_errada)])
		print('\nPalavra: ' + self.esconder_palavra())
		print('\nLetras Erradas: ',)
		for letra in self.letra_errada:
			print(letra)
		print('\nLetras corretas: ',)
		for letra in self.letra_certa:
			print(letra)
		print()

# Função para ler uma palavra de forma aleatória do banco de palavras
def palavra_aleatoria():
        with open("palavras.txt", "rt") as pa:
                banco_palavras = pa.readlines()
        return banco_palavras[random.randint(0,len(banco_palavras))].strip()


# Função Main - Execução do Programa >>>PROGRAMA PRINCIPAL<<<<
def main():

	# Objeto
	jogo = enforcado(palavra_aleatoria())

	# Enquanto o jogo não tiver terminado, print do status, solicita uma letra e faz a leitura do caracter
	while not jogo.jogo_terminou():
		jogo.print_status_jogo()
		usuario_input = input('Digirte uma Letra: ')
		jogo.adivinhar(usuario_input)

	# Verifica o status do jogo
	jogo.print_status_jogo()

	# De acordo com o status, imprime mensagem na tela para o usuário
	if jogo.jogador_venceu():
		print('\nParabéns! Você venceu!!')
	else:
		print('\nGame over! Você perdeu.')
		print('A palavra era ' + jogo.palavra)

	print('\nFoi bom jogar com você! Agora vá estudar!\n')

# Executa o programa
if __name__ == "__main__":
	main()

	

# -*- coding: utf-8 -*-

# Hangman Game (Jogo da Forca)
# Programação Orientada a Objetos

# Import
import random

# Board (tabuleiro)
board = ['''

>>>>>>>>>>Hangman<<<<<<<<<<

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
class Hangman:

	# Método Construtor
	def __init__(self, word):
		self.word = word
		self.letrasErradas = []
		self.letrasCertas = []

	# Método para adivinhar a letra
	def guess(self, letra):
		if letra in self.word and letra not in self.letrasCertas:
			self.letrasCertas.append(letra)
		elif letra not in self.word and letra not in self.letrasErradas:
			self.letrasErradas.append(letra)
		else:
			return False
		return True

	# Método para verificar se o jogo terminou
	def hangman_over(self):
		return self.hangman_won() or (len(self.letrasErradas) == (len(board)-1))
		
	# Método para verificar se o jogador venceu
	def hangman_won(self):
		if '_' not in self.hide_word():
			return True
		else:
			return False

	# Método para não mostrar a letra no board
	def hide_word(self):
		letras=''
		for l in self.word:
			if l not in self.letrasCertas:
				letras += '_'
			else:
				letras += l
		return letras
		
	# Método para checar o status do game e imprimir o board na tela
	def print_game_status(self):
		print(board[len(self.letrasErradas)])
		print('Palavra: '+ self.hide_word())
		print('Letras Erradas: ',)
		print(list(self.letrasErradas))
		print('='*30)
		print('Letras Corretas: ',)
		print(list(self.letrasCertas))
		print('='*30)

# Função para ler uma palavra de forma aleatória do banco de palavras
def rand_word():
        with open("palavras.txt", "rt") as f:
                bank = f.readlines()
        return bank[random.randint(0,(len(bank)-1))].strip()


# Função Main - Execução do Programa
def main():
	#Repete o Jogo até o jogador resolver parar
	while input('Deseja jogar? (sim ou nao) ').lower() == 'sim':
		# Objeto
		game = Hangman(rand_word())
		# Enquanto o jogo não tiver terminado, print do status, solicita uma letra e faz a leitura do caracter
		while not game.hangman_over():
			game.print_game_status()
			letra = input('Informe uma letra: ')
			game.guess(letra)

		# Verifica o status do jogo
		game.print_game_status()

		# De acordo com o status, imprime mensagem na tela para o usuário
		if game.hangman_won():
			print ('\nParabéns! Você venceu!!')
		else:
			print ('\nGame over! Você perdeu.')
			print ('A palavra era ' + game.word)

		print ('\nFoi bom jogar com você! Agora vá estudar!\n')

# Executa o programa		
if __name__ == "__main__":
	main()


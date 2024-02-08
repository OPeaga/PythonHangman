# Projeto Jogo da Forca

import random
from os import system, name

palavras = [
"carro", "casa", "gato", "cachorro", "amigo", "computador", "livro", "mesa", "avião", "árvore",
"flor", "rio", "praia", "montanha", "sol", "lua", "estrela", "céu", "terra", "mar",
"lago", "pássaro", "peixe", "telefone", "internet", "rede", "amor", "família", "felicidade",
"tristeza", "esperança", "sonho", "realidade", "festa", "música", "dança", "escola", "professor",
"aluno", "caneta", "papel", "tinta", "cor", "pintura", "escultura", "cinema", "teatro",
"viagem", "aventura", "exploração"
]



def limpa_tela():
     # Se windows comando cls para limpar tela
     if name == "nt":
          _= system('cls')
     # Se for Mac ou Linux
     else:
          _= system('clear')
          

def generateWord():
     chosenWord = random.choice(palavras)
     palavras.remove(chosenWord)
     return chosenWord

def game():
     
     guessedLetters = []
     chances = 6
     
     limpa_tela()
     print("Bem vindos ao Jogo da Forca do PH\n")
     print("Adivinhe se for capaz!\n")
     
     palavra = generateWord()
     letrasDescobertas = ['_' for letra in palavra]
     letrasErradas = []
     
     print(palavra)
     print(letrasDescobertas)
     print(letrasErradas)
     
     while chances > 0:
          print("".join(letrasDescobertas))
          print("%d chances"%(chances))
          print("letras erradas: ", "".join(letrasErradas))
          
          tentativa = input("\nDigite uma letra").lower()
          
          if tentativa in palavra:
               index  = 0
               for letra in palavra:
                    if tentativa == letra:
                         letrasDescobertas[index] = letra
                         index +=1
          else:
               chances -=1
               letrasErradas.append(tentativa)
               
          if "_" not in letrasDescobertas:
               print("\nVoce venceu, a palvra era: ", palavra)
          
     if "_" in letrasDescobertas:
          print("\nVoce perdeu! A palavra era: ",palavra)

# Bloco main
if __name__ == "main":
     game()
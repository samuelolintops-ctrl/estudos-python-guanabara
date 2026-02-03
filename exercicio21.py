#=========== Desafio 21 ===========
# Faça um programa em python que abra e reproduza o áudio de um arquivo MP3

from pygame import mixer

# Inicializa
mixer.init()

# Carrega o áudio
mixer.music.load("Alarm01.wav")

# Dá play no áudio
mixer.music.play()
input() # Segura o programa

# Encerra a música
mixer.music.stop()
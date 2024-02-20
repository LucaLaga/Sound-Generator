import pygame
import time

pygame.init()

# Funzione che riproduce i file .wav generati
def playSounds():
    # Root Note
    pygame.mixer.music.load("1.wav")
    pygame.mixer.music.play()
    pygame.event.wait()

    time.sleep(2)
    
    # Second Note
    pygame.mixer.music.load("2.wav")
    pygame.mixer.music.play()
    pygame.event.wait()

    time.sleep(2)

    # Third Note
    pygame.mixer.music.load("3.wav")
    pygame.mixer.music.play()
    pygame.event.wait()


    time.sleep(3)


    # Chord
    pygame.mixer.music.load("chord.wav")
    pygame.mixer.music.play()
    pygame.event.wait()

    time.sleep(3)

    # Harmonics
    pygame.mixer.music.load("harmonics.wav")
    pygame.mixer.music.play()
    pygame.event.wait()

    time.sleep(2)
import pygame
import time

pygame.init()
def playSounds():
    pygame.mixer.music.load("1.wav")
    pygame.mixer.music.play()
    pygame.event.wait()

    time.sleep(2)
    
    pygame.mixer.music.load("2.wav")
    pygame.mixer.music.play()
    pygame.event.wait()

    time.sleep(2)

    pygame.mixer.music.load("3.wav")
    pygame.mixer.music.play()
    pygame.event.wait()


    time.sleep(3)


    pygame.mixer.music.load("chord.wav")
    pygame.mixer.music.play()
    pygame.event.wait()

    time.sleep(3)

    pygame.mixer.music.load("harmonics.wav")
    pygame.mixer.music.play()
    pygame.event.wait()

    time.sleep(2)
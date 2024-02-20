from generator import get_noteFrequency, getRightFreq, generate_noteWave, generate_chordWave, generate_HarmonicWave, generate_chordFreqs
from player import playSounds
import matplotlib.pyplot as plt
import numpy as np
from scipy.io import wavfile

DURATION = 2
SAMPLE_RATE = 44100
T = np.linspace(0, DURATION, int(DURATION * SAMPLE_RATE))

def menu():
    choice = int(input("1. Inserisci la frequenza\n2. Inserisci il nome della nota\n--> "))

    match choice:
        case 1:
            rootFrequency = getRightFreq(float(input("Inserisci la frequenza: ")))
        case 2:
            note_name = input("Inserisci il nome della nota (in inglese): ")
            octave = int(input("Inserisci l'ottava (da 0 a 8): "))

            rootFrequency = get_noteFrequency(note_name, octave)
    
    """
    1. Major
    2. Minor
    3. Diminished
    4. Sus2
    5. Sus4
    6. Augmented
    """
    chordType = int(input("Inserisci il tipo di accordo (Da 1 a 6): "))
        
    return rootFrequency, chordType

def wave_generator(rootFrequency, chordType):
    note1Wave = (generate_noteWave(rootFrequency, DURATION, SAMPLE_RATE) * 32767).astype(np.int16)
    chordWave = (generate_chordWave(rootFrequency, DURATION, chordType, SAMPLE_RATE) * 32767).astype(np.int16)
    harmonicWave = (generate_HarmonicWave(rootFrequency, DURATION, SAMPLE_RATE) * 32767).astype(np.int16)

    frequencies = generate_chordFreqs(rootFrequency, chordType)
    note2Wave = (generate_noteWave(frequencies[1], DURATION, SAMPLE_RATE) * 32767).astype(np.int16)
    note3Wave = (generate_noteWave(frequencies[2], DURATION, SAMPLE_RATE) * 32767).astype(np.int16)

    return note1Wave, note2Wave, note3Wave, chordWave, harmonicWave

def file_writer(note1Wave, note2Wave, note3Wave, chordWave, harmonicWave):
    wavfile.write("1.wav", SAMPLE_RATE, note1Wave)
    wavfile.write("2.wav", SAMPLE_RATE, note2Wave)
    wavfile.write("3.wav", SAMPLE_RATE, note3Wave)

    wavfile.write("chord.wav", SAMPLE_RATE, chordWave)

    wavfile.write("harmonics.wav", SAMPLE_RATE, harmonicWave)

def plot_generator(note1Wave, note2Wave, note3Wave, chordWave, harmonicWave):
    plt.subplot(3, 1, 1)
    plt.plot(T[:1024], note1Wave[:1024], label="Note 1")
    plt.plot(T[:1024], note2Wave[:1024], label="Note 2")
    plt.plot(T[:1024], note3Wave[:1024], label="Note 3")
    plt.legend()

    plt.subplot(3, 1, 2)
    plt.plot(chordWave[:1024])

    plt.subplot(3, 1, 3)
    plt.plot(harmonicWave[:1024])

    plt.tight_layout()
    plt.show()

def main():
    rootFrequency, chordType = menu()
    note1Wave, note2Wave, note3Wave, chordWave, harmonicWave = wave_generator(rootFrequency, chordType)

    file_writer(note1Wave, note2Wave, note3Wave, chordWave, harmonicWave)

    playSounds()

    plot_generator(note1Wave, note2Wave, note3Wave, chordWave, harmonicWave)


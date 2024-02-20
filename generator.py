import numpy as np

def get_noteFrequency(name, octave):
    note = ['C', 'C#', 'D', 'Eb', 'E', 'F', 'F#', 'G', 'G#', 'A', 'Bb', 'B']
    frequencies = [[16.35, 17.32, 18.35, 19.45, 20.6, 21.83, 23.12, 24.50, 25.96, 27.50, 29.14, 30.87],
                   [32.7, 34.65, 36.71, 38.89, 41.2, 43.65, 46.25, 49, 51.91, 55, 58.27, 61.74],
                   [65.41, 69.3, 73.42, 77.78, 82.41, 87.31, 92.5, 98, 103.8, 110, 116.5, 123.5],
                   [130.8, 138.6, 146.8, 155.6, 164.8, 174.6, 185, 196, 207.7, 220, 233.1, 246.9],
                   [261.6, 277.2, 293.7, 311.1, 329.6, 349.2, 370, 392, 415, 440, 466.2, 493.9],
                   [523.3, 554.4, 587.3, 622.3, 659.3, 698.5, 740, 784, 830.6, 880, 932.3, 987.8],
                   [1047, 1109, 1175, 1245, 1319, 1397, 1480, 1568, 1661, 1760, 1865, 1976],
                   [2093, 2217, 2349, 2489, 2637, 2794, 2960, 3136, 3322, 3520, 3729, 3951],
                   [4186, 4435, 4699, 4978,5274, 5588, 5920, 6272, 6645, 7040, 7459, 7902]]
    
    return frequencies[octave][note.index(name)]

def getRightFreq(frequency):
    note = ['C', 'C#', 'D', 'Eb', 'E', 'F', 'F#', 'G', 'G#', 'A', 'Bb', 'B']
    frequencies0 = np.array([16.35, 17.32, 18.35, 19.45, 20.6, 21.83, 23.12, 24.50, 25.96, 27.50, 29.14, 30.87])
    frequencies1 = np.array([32.7, 34.65, 36.71, 38.89, 41.2, 43.65, 46.25, 49, 51.91, 55, 58.27, 61.74])
    frequencies2 = np.array([65.41, 69.3, 73.42, 77.78, 82.41, 87.31, 92.5, 98, 103.8, 110, 116.5, 123.5])
    frequencies3 = np.array([130.8, 138.6, 146.8, 155.6, 164.8, 174.6, 185, 196, 207.7, 220, 233.1, 246.9])
    frequencies4 = np.array([261.6, 277.2, 293.7, 311.1, 329.6, 349.2, 370, 392, 415, 440, 466.2, 493.9])
    frequencies5 = np.array([523.3, 554.4, 587.3, 622.3, 659.3, 698.5, 740, 784, 830.6, 880, 932.3, 987.8])
    frequencies6 = np.array([1047, 1109, 1175, 1245, 1319, 1397, 1480, 1568, 1661, 1760, 1865, 1976])
    frequencies7 = np.array([2093, 2217, 2349, 2489, 2637, 2794, 2960, 3136, 3322, 3520, 3729, 3951])
    frequencies8 = np.array([4186, 4435, 4699, 4978,5274, 5588, 5920, 6272, 6645, 7040, 7459, 7902])

    distances = np.array([
        np.absolute(frequencies0-frequency),
        np.absolute(frequencies1-frequency),
        np.absolute(frequencies2-frequency),
        np.absolute(frequencies3-frequency),
        np.absolute(frequencies4-frequency),
        np.absolute(frequencies5-frequency),
        np.absolute(frequencies6-frequency),
        np.absolute(frequencies7-frequency),
        np.absolute(frequencies8-frequency)
        ])
    
    octave = np.where(distances == np.min(distances))[0][0]
    index = 0
    value = 0

    match octave:
        case 0:
            index = np.where(distances[octave] == np.min(distances[octave]))[0][0]
            value = frequencies0[index]
        case 1:
            index = np.where(distances[octave] == np.min(distances[octave]))[0][0]
            value = frequencies1[index]
        case 2:
            index = np.where(distances[octave] == np.min(distances[octave]))[0][0]
            value = frequencies2[index]
        case 3:
            index = np.where(distances[octave] == np.min(distances[octave]))[0][0]
            value = frequencies3[index]
        case 4:
            index = np.where(distances[octave] == np.min(distances[octave]))[0][0]
            value = frequencies4[index]
        case 5:
            index = np.where(distances[octave] == np.min(distances[octave]))[0][0]
            value = frequencies5[index]
        case 6:
            index = np.where(distances[octave] == np.min(distances[octave]))[0][0]
            value = frequencies6[index]
        case 7:
            index = np.where(distances[octave] == np.min(distances[octave]))[0][0]
            value = frequencies7[index]
        case 8:
            index = np.where(distances[octave] == np.min(distances[octave]))[0][0]
            value = frequencies8[index]
    

    return value

def generate_chordFreqs(rootFreq, chordType=1):
    match chordType:
        case 1:
            return np.array([rootFreq, (5 / 4) * rootFreq, (3 / 2) * rootFreq])
        case 2:
            return np.array([rootFreq, (6 / 5) * rootFreq, (3 / 2) * rootFreq])
        case 3:
            return np.array([rootFreq, (6 /5) * rootFreq, (45 / 32) * rootFreq])
        case 4:
            return np.array([rootFreq, (9 / 8) * rootFreq, (3 / 2) * rootFreq])
        case 5:
            return np.array([rootFreq, (4 / 3) * rootFreq, (3 / 2) * rootFreq])
        case 6:
            return np.array([rootFreq, (5 / 4) * rootFreq, (8 / 5) * rootFreq])

def generate_HarmonicFreqs(rootFreq):
    frequencies = np.zeros(16)
    for i in range(16):
        frequencies[i] = rootFreq / (1 / (i + 1))
    
    return frequencies



def generate_noteWave(freq, duration, sample_rate=44100):
    t = np.linspace(0, duration, int(duration*sample_rate))

    wave = np.sin(2 * np.pi * freq * t)

    maxValue = np.max(np.abs(wave))
    if maxValue > 0:
        wave /= maxValue
    
    return wave

def generate_chordWave(freq, duration, chordType=1, sample_rate=44100):
    frequencies = generate_chordFreqs(freq, chordType)
    
    t = np.linspace(0, duration, int(duration * sample_rate))
    wave = np.zeros(len(t))

    wave += np.sin(2 * np.pi * frequencies[0] * t)
    wave += np.sin(2 * np.pi *frequencies[1] * t)
    wave += np.sin(2 * np.pi *frequencies[2] * t)
    
    maxValue = np.max(np.abs(wave))
    if maxValue > 0:
        wave /= maxValue
    
    return wave

def generate_HarmonicWave(freq, duration, sample_rate=44100):
    frequencies = generate_HarmonicFreqs(freq)

    t = np.linspace(0, duration, int(duration * sample_rate))

    wave = np.zeros(len(t))

    for f in frequencies:
        wave += np.sin(2 * np.pi * f * t)
    
    maxValue = np.max(np.abs(wave))
    if maxValue > 0:
        wave /= maxValue
    
    return wave
import numpy as np

NOTE_NAMES = ['C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B']

def freq_to_note(freq):
    if freq == 0: return None
    A4 = 440
    C0 = A4 * pow(2, -4.75)
    h = round(12 * np.log2(freq / C0))
    octave = h // 12
    n = h % 12
    return f"{NOTE_NAMES[n]}{octave}"

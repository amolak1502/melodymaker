import numpy as np
import random
from scipy.io.wavfile import write

sample_rate = 44100 #Hz

def get_wave(freq,duration = 0.25):
    amplitude =  4096 
    t = np.linspace(0 , duration , int(sample_rate*duration))
    wave = amplitude * np.sin(2 * np.pi * freq * t)

    return wave 

def get_piano_notes(octave_freq):

    octave = ['C' , 'c' , 'D' , 'd' , 'E' , 'F' , 'f' , 'G' , 'g' , 'A' , 'a' , 'B']
    base_freq = octave_freq

    note_freqs = {octave[i]:base_freq*pow (2,(i/12)) for i in range(len(octave))}
    note_freqs[''] = 0.0

    return note_freqs

def get_song_data(music_notes_new):
    note_freqs = get_piano_notes(octave_freq[1])
    song = [get_wave(note_freqs[note]) for note in music_notes_new]
    song = np.concatenate(song)

    return(song)

cmajor = ['C','D','E','F','G','A','B','','','']
octave_freq = [130.81,261.63,523.25,1046.502]



if __name__ == '__main__':
    music_notes_new = []

    name = input('Enter the name of the file:')
    

    for i in range(20):
        rand = random.randint(0,9)
        music_notes_new.append(cmajor[rand])

    print('gg')
    print(music_notes_new)
    
    data = get_song_data(music_notes_new)

    data = data * (16300)/np.max(data)

    write(name + '.wav' , sample_rate, data.astype(np.int16))
    print('Song Written Successfully')
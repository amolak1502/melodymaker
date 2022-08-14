import numpy as np
import random
from scipy.io.wavfile import write

sample_rate = 44100 #Hz

def get_wave(freq,duration = 0.25, amplitude=4096):
    t = np.linspace(0 , duration , int(sample_rate*duration))
    wave = amplitude * np.sin(2 * np.pi * freq * t)

    return wave 

def get_piano_notes():

    octave = ['C' , 'c' , 'D' , 'd' , 'E' , 'F' , 'f' , 'G' , 'g' , 'A' , 'a' , 'B']
    base_freq = 261.63

    note_freqs = {octave[i]:base_freq*pow (2,(i/12)) for i in range(len(octave))}
    note_freqs[''] = 0.0

    return note_freqs

def get_song_data(music_notes_new, duration, amplitude):
    note_freqs = get_piano_notes()
    song = [get_wave(note_freqs[note], duration, amplitude) for note in music_notes_new]
    song = np.concatenate(song)

    return(song)

cmajor = ['C','D','E','F','G','A','B','C','D','E','F','G','A']
cmelody = ['C','D','E','F','G','A','B','','','']


if __name__ == '__main__':
    music_notes_new = []

    j = random.randint(1,6)
    print(j)
    k = random.randint(1,6)
    l = random.randint(1,6)
    chord_note_1 = ['C','','','',cmajor[j],'','','',cmajor[k],'','','',cmajor[l],'','','']
    chord_note_2 = ['E','','','',cmajor[j+3],'','','',cmajor[k+3],'','','',cmajor[l+3],'','','']
    chord_note_3 = ['G','','','',cmajor[j+5],'','','',cmajor[k+5],'','','',cmajor[l+5],'','','']

    name = input('Enter the name of the file:')
    

    for i in range(16):
        rand = random.randint(0,9)
        music_notes_new.append(cmelody[rand])

    print('gg')
    print(music_notes_new)
    
    data = get_song_data(music_notes_new,0.25,4096)
    data2 = get_song_data(chord_note_1,0.25,800)
    data3 = get_song_data(chord_note_2,0.25,800)
    data4 = get_song_data(chord_note_3,0.25,800)

    data = (data+data2+data3+data4) * (16300)/np.max(data)

    write(name + '.wav' , sample_rate, data.astype(np.int16))
    print('Song Written Successfully')

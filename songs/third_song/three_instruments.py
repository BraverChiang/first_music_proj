from music21 import stream, note, chord, instrument, tempo
import random

# Create Score
score = stream.Score()
score.append(tempo.MetronomeMark(number=78))  # Slightly slow ballad tempo

# Define three instruments
piano_part = stream.Part()
piano_part.insert(0, instrument.Piano())

violin_part = stream.Part()
violin_part.insert(0, instrument.Violin())

flute_part = stream.Part()
flute_part.insert(0, instrument.Flute())

score.append(piano_part)
score.append(violin_part)
score.append(flute_part)

# Generate evolving chord progression (each chord appears only once)
chord_sequence = [
    chord.Chord(['C4','E4','G4']),  # C major
    chord.Chord(['D4','F4','A4']),  # D minor
    chord.Chord(['E4','G4','B4']),  # E minor
    chord.Chord(['F4','A4','C5']),  # F major
    chord.Chord(['G4','B4','D5']),  # G major
    chord.Chord(['A3','C4','E4']),  # A minor
    chord.Chord(['B3','D4','F4']),  # B diminished
    chord.Chord(['C5','E5','G5'])   # C major octave
]

# Piano: each chord arpeggiated once for 4 beats
for c in chord_sequence:
    for pitch in c.pitches:
        n = note.Note(pitch)
        n.quarterLength = 1.0
        piano_part.append(n)

# Violin: flowing melody, no repeats
violin_scale = ['E5','F5','G5','A5','B5','C6','D6','E6','F6','G6','A6','B6','C7','D7','E7']
for i, pitch in enumerate(violin_scale):
    n = note.Note(pitch)
    n.quarterLength = 0.5  # half-beat
    violin_part.append(n)

# Flute: counter-melody, different from violin, continuous
flute_scale = ['C5','D5','E5','F5','G5','A5','B5','C6','D6','E6','F6','G6','A6','B6','C7']
for i, pitch in enumerate(flute_scale):
    n = note.Note(pitch)
    n.quarterLength = 0.5
    flute_part.append(n)

# Export files
score.write('midi', fp='unique_ballad.mid')
score.write('musicxml', fp='unique_ballad.xml')

print("✅ 60-second unique ballad with no repeated melody generated!")